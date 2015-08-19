"""Demo settings and globals."""

from base import *

for logger_key in LOGGING['loggers'].keys():
    if logger_key == 'root': continue
    LOGGING['loggers'][logger_key]['handlers'] = ['console', 'var_log']