"""Test run settings and globals."""

from base import *

""" DEBUG CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
TEST = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

""" LOGGING """
for logger_key in LOGGING['loggers'].keys():
    LOGGING['loggers'][logger_key]['level'] = 'DEBUG'

for handler_key in LOGGING['handlers'].keys():
    LOGGING['handlers'][handler_key]['level'] = 'DEBUG'

""" TEST SPEED CHEAT """
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

""" TEST RUNNER """
TEST_RUNNER = "readonly.test_runner.LegacyDiscoverRunner"

# Test user should be local superuser (if our example was more than SQLite)
# Since the tests are never run in production the creds don't have to go into secrets file.

# for db_key in DATABASES.keys():
#     DATABASES[db_key]['USER'] = 'readonly_test'
#     DATABASES[db_key]['PASSWORD'] = 'secret'
