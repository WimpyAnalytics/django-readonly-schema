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
SUPERVISOR_CONF = os.path.join(SETTINGS_ROOT, 'supervisor.conf')
SECRETS = os.path.join(SETTINGS_ROOT, '_secrets.py')
SECRETS_TEMPLATE = os.path.join(SETTINGS_ROOT, '_secrets.template.ini')
STATIC_ROOT = os.path.join(project.project_paths.root, 'static')


@task()
def runserver():
    """Runs the server using gunicorn"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readonly.settings.local")
    with safe_cd(paths.project_paths.manage_root):
        if not os.path.exists(SECRETS):
            shutil.copy(SECRETS_TEMPLATE, SECRETS)

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
        'fpm', '-s', 'dir', '-t', 'deb', '-n', name, '-v', version, '-d', 'python,python-dev,supervisor',
        '{source}={target}'.format(source=project.project_paths.manage_root, target='/srv/django-readonly/readonly'),
        '{source}={target}'.format(source=project.project_paths.venv, target='/srv/django-readonly/venv'),
        '{source}={target}'.format(source=STATIC_ROOT, target='/srv/django-readonly/static'),
        '{source}={target}'.format(source=SUPERVISOR_CONF, target='/etc/supervisor/conf.d/{}'.format(name)),
    )
    print('This deb can now be installed on a Ubuntu 12.04 with gdebi.')
    print('> sudo apt-get install gdebi (one time only)')
    print('> sudo gdebi django-readonly_{}_amd64.deb'.format(version))