bind = '0.0.0.0:8000'  # The address and port on which the Gunicorn server will listen
workers = 3  # The number of worker processes for handling requests
timeout = 30  # The maximum time in seconds for a worker to process a request

loglevel = 'info'  # The log level

# The Python path to the Django application's WSGI application
# pythonpath = './venv/bin/python'
chdir = 'project'

wsgi_app = 'project.wsgi:application'

# To disable the Python stdout buffering
raw_env = ["PYTHONUNBUFFERED=1"]
