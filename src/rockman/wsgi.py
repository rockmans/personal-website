"""
WSGI config for rockman project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rockman.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import newrelic.agent

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
newrelic.agent.initialize('/src/newrelic.ini', os.environ.get("APP", "test"))
application = newrelic.agent.WSGIApplicationWrapper(application)
