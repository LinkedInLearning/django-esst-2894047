"""
WSGI config for smartnotes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'smartnotes.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'smartnotes.settings'
print(f"Using settings module: {settings_module}")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
application = get_wsgi_application()