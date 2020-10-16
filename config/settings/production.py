"""Production configuration"""

from .base import *

import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DJANGO_DEBUG') or False
ALLOWED_HOSTS = []
