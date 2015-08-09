#!/usr/bin/python
import os
MODULE_PATH = os.path.abspath(__file__)

import pyntofdjango
pyntofdjango.setup_pod(MODULE_PATH)
from pyntofdjango.tasks import pip, python, clean, create_venv, manage, recreate_venv, runserver, migrate, \
    docs, venv_bin, delete_venv, dumpdata

from pyntofdjango.tasks import test_manage as test

from pyntofdjango import project
from pynt import task

