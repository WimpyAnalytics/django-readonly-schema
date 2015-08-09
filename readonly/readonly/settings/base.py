"""Common settings and globals."""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from sys import path

""" PATH CONFIGURATION """
# Absolute filesystem path to the Django project directory:
MODULE_ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG_APP_ROOT = os.path.dirname(MODULE_ROOT)
MANAGE_ROOT = os.path.dirname(CONFIG_APP_ROOT)
REPO_ROOT = os.path.dirname(MANAGE_ROOT)
SECRETS_MODULE = '_secrets'  # This file is *not* sourced.
STATIC_ROOT = os.path.join(REPO_ROOT, 'static')

# Site name:
SITE_NAME = os.path.basename(MANAGE_ROOT)

# Obtaining secrets
try:
    from . import _secrets
except ImportError:
    raise ImportError('Could not import _secrets module. Please create it by using _secrets.template.py as a template.')

_version = None
ENVIRONMENT = os.environ.get('DJANGO_SETTINGS_MODULE').replace('readonly.settings.', '')

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(MANAGE_ROOT)

""" DEBUG CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

""" MANAGER CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Engineering', 'eng@acme.com'),
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'server@acme.com'
DEFAULT_FROM_EMAIL = 'Server <server@acme.com>'

""" DATABASE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Our cheat: 'default' serves as a dumping ground for the migrations tables we won't use.
    # SQLite is ok for this since we don't care about it's contents.
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(MANAGE_ROOT, 'db.sqlite3'),
    },
    'legacy': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(MANAGE_ROOT, 'legacy-db.sqlite3'),
        # If we had needed credentials
        #'USER': _secrets.db_read_username,
        #'PASSWORD': _secrets.db_read_password,
    },
}

""" GENERAL CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Chicago'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

""" MEDIA CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.normpath(os.path.join(MANAGE_ROOT, 'media'))
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

""" STATIC FILE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(MANAGE_ROOT, 'static')),
)
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

""" SECRET CONFIGURATION """
SECRET_KEY = _secrets.secret_key

""" SITE CONFIGURATION """
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

""" FIXTURE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    os.path.normpath(os.path.join(MANAGE_ROOT, 'fixtures')),
)

""" TEMPLATE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    # These will come into play when we have a user interface.
    #'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(MANAGE_ROOT, 'templates')),
)

""" MIDDLEWARE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

""" URL CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME

""" APP CONFIGURATION """
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
)
# Apps specific for this project go here.
LOCAL_APPS = (
    'legacy',
)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

""" LOGGING CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'raiseExceptions': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        "null": {
            "class": "logging.NullHandler"
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        "root": {
            "level": "NOTSET",
            "handlers": ["null"]
        },
        'readonly': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'diagnostics': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

""" WSGI CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

""" LEGACY/CUSTOM DATABASE SUPPORT """
DATABASE_ROUTERS = ['readonly.routers.LegacyDatabaseRouter']

""" EMAIL CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
