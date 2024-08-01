#!/usr/bin/env python
import os
import sys
import django
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobs.settings')
django.setup()
application = WSGIHandler()

# def lambda_handler(event, context):
#     from mangum import Mangum
#     handler = Mangum(application)
#     return handler(event, context)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobs.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
