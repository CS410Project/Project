import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing
import os

if not os.path.exists('log'):
    os.mkdir('log')

debug = True
loglevel = 'debug'
bind = '127.0.0.1:5000'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
errorlog = 'log/error.log'
accesslog = 'log/access.log'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'
