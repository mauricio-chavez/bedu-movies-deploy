from config.settings.base import INSTALLED_APPS
"""Local settings for development purposes"""

from .base import *

SECRET_KEY = 'u5v1f29=_^(@)6ufgi4)noan%m8fot2=z%70=o&s)@c=33ei0+'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'django_extensions'
]
