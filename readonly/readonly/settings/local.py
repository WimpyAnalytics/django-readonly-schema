""" Local dev settings and globals. """

from base import *

""" DEBUG CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG

""" LOGGING """
for logger_key in LOGGING['loggers'].keys():
    LOGGING['loggers'][logger_key]['level'] = 'DEBUG'

for handler_key in LOGGING['handlers'].keys():
    LOGGING['handlers'][handler_key]['level'] = 'DEBUG'

""" TOOLBAR CONFIGURATION """
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
# Should be added as soon as possible in the order
MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TEMPLATE_CONTEXT': True,
}