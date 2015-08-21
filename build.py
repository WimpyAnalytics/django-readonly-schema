#!/usr/bin/python
import shutil
import os
MODULE_PATH = os.path.abspath(__file__)

import pyntofdjango
pyntofdjango.setup_pod(MODULE_PATH)
from pyntofdjango.tasks import pip, python, clean, create_venv, manage, recreate_venv, runserver, migrate, \
    docs, venv_bin, delete_venv, dumpdata

from pyntofdjango.tasks import test_manage as test

from pyntcontrib import safe_cd
from pyntofdjango import project, paths
from pynt import task

SETTINGS_ROOT = os.path.join(paths.project_paths.manage_root, 'readonly/settings')
STATIC_ROOT = os.path.join(project.project_paths.root, 'static')
DEPLOY_EXTRAS_DIR = os.path.join(project.project_paths.root, 'deploy_extras')


@task()
def runserver():
    """Runs the server using gunicorn"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readonly.settings.local")
    with safe_cd(paths.project_paths.manage_root):
        project.venv_execute(
           'gunicorn',
           '--reload',
           '-b', '0.0.0.0:8000',
           '--access-logfile', '-',
           'readonly.wsgi',
       )


@task(create_venv)
def create_deb():
    """Creates a deb using the present vevnv"""
    version = '0.0.1'
    name = 'django-readonly'
    project.execute(
        'fpm', '-s', 'dir', '-t', 'deb', '-n', name, '-v', version, '-d', 'python,python-dev',
        '--after-install', os.path.join(DEPLOY_EXTRAS_DIR, 'after-install.sh'),
        '--before-upgrade', os.path.join(DEPLOY_EXTRAS_DIR, 'before-upgrade.sh'),
        '--after-upgrade', os.path.join(DEPLOY_EXTRAS_DIR, 'after-upgrade.sh'),
        '{source}/={target}/'.format(source=project.project_paths.manage_root, target='/srv/django-readonly/readonly'),
        '{source}/={target}/'.format(source=project.project_paths.venv, target='/srv/django-readonly/venv'),
        '{source}/={target}/'.format(source=STATIC_ROOT, target='/srv/django-readonly/static'),
        '{source}={target}'.format(source=os.path.join(SETTINGS_ROOT, 'upstart.conf'), target='/etc/init/django-readonly.conf'),
    )
    print('This deb can now be installed on a Ubuntu 12.04 server. But requires gdebi to be installed form local file.')
    print('(on server, one time) sudo apt-get update && apt-get install gdebi')
    print('(on server) sudo gdebi django-readonly_{}_amd64.deb'.format(version))