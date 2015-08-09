import contextlib
import os
import logging

from django.test.runner import DiscoverRunner
from django.conf import settings
import sqlite3

logger = logging.getLogger(__name__)


class LegacyDiscoverRunner(DiscoverRunner):
    """
    See https://docs.djangoproject.com/en/1.7/topics/testing/advanced/#defining-a-test-runner
    """

    @contextlib.contextmanager
    def _safe_cd(self, path):
        """
        Usage:
        with _safe_cd(gitrepo_path):
            subprocess.call('git status')
        """
        starting_directory = os.getcwd()
        try:
            os.chdir(path)
            yield
        finally:
            os.chdir(starting_directory)

    def setup_databases(self, **kwargs):
        """Though our schema is readonly in shared environments we assume DB control in testing"""

        # Super will create an empty test_<db name> automatically
        config = super(LegacyDiscoverRunner, self).setup_databases(**kwargs)

        # Invoke any custom ddl to create the schema after that.
        script_path = os.path.join(settings.MANAGE_ROOT, 'legacy-schema.sql')
        logger.info("Initializing DB with script. [Path: {}]".format(script_path))
        with open(script_path, 'r') as sql_file:
            ddl = sql_file.read()
            conn = sqlite3.connect(settings.DATABASES['legacy']['NAME'])
            conn.execute(ddl)

        return config