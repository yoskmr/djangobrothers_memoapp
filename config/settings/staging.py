import os
from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []  # TODO for staging domain

# TODO stating databse

# TODO stating static server
