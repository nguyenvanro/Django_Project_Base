from .base import *

DEBUG = True

ALLOWED_HOSTS += ['.localhost', '127.0.0.1']

# Cấu hình database development
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

# Các cấu hình khác dành cho môi trường dev