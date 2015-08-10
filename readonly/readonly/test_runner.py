import contextlib
import os
import logging

from django.test.runner import DiscoverRunner
from django.conf import settings
from django.db import connections

logger = logging.getLogger(__name__)


class LegacyDiscoverRunner(DiscoverRunner):
    """
    See https://docs.djangoproject.com/en/1.7/topics/testing/advanced/#defining-a-test-runner
    """

    def setup_databases(self, **kwargs):
        """Though our schema is readonly in shared environments we assume DB control in testing"""

        # Super will create an empty test_<db name> automatically
        config = super(LegacyDiscoverRunner, self).setup_databases(**kwargs)

        # Invoke any custom ddl to create the schema after that.
        script_path = os.path.join(settings.MANAGE_ROOT, 'legacy-schema.sql')
        logger.info("Initializing DB with script. [Path: {}]".format(script_path))
        with open(script_path, 'r') as sql_file:
            ddl = sql_file.read()

        cursor = connections['legacy'].cursor()
        cursor.executescript(ddl)

        return config