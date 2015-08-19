import multiprocessing

bind = "0.0.0.0:80"
workers = multiprocessing.cpu_count() * 2 + 1

errorlog = '/var/log/django-readonly-schema/error.log'
accesslog = '/var/log/django-readonly-schema/access.log'