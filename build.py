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
SECRETS = os.path.join(SETTINGS_ROOT, '_secrets.py')
SECRETS_TEMPLATE = os.path.join(SETTINGS_ROOT, '_secrets.template.ini')


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
