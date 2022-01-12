"""
ASGI config for roni_analytics_task project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesApp.settings')

application = get_wsgi_application()
import os

from django.core.wsgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roni_analytics_task.settings')

application = get_asgi_application()
