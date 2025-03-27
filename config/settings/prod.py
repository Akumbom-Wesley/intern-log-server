from .base import *
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["intern-log.onrender.com"]

# Render PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}

SECURE_HSTS_SECONDS = 30 * 24 * 60 * 60  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = config('SECRET_KEY')

# Only enable Swagger in development
if DEBUG:
    SWAGGER_SETTINGS['VALIDATOR_URL'] = None  #

# Keep strict control in production
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='intern-log.onrender.com',
    cast=Csv()
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Required for drf-yasg static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]