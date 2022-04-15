import os

from .common import *
from .partials.utils import get_secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')

############
# DATABASE #
############
if get_secret('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_secret('DATABASE_NAME'),
            'USER': get_secret('DATABASE_USER'),
            'PASSWORD': get_secret('DATABASE_PASSWORD'),
            'HOST': get_secret('DATABASE_HOST'),
            'PORT': get_secret('DATABASE_PORT'),
        }
    }

########
# CORS #
########
CORS_ALLOWED_ORIGINS = get_secret('CORS_ALLOWED_ORIGINS')
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'instance',
    'access',
]

###########
# STORAGE #
###########
USE_S3 = get_secret('DEBUG') == "True"

if USE_S3:
    # AWS settings
    AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_ACL = None

    # S3 static files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'project_name.storage_backends.StaticStorage'

    # S3 media files
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'project_name.storage_backends.PublicMediaStorage'
