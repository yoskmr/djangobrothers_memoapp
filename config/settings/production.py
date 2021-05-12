import os
from .base import *


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []  # TODO for production domain


# TODO production databse


# TODO production static server
