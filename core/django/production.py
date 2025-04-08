from decouple import config
from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

DOMAIN = ''

ALLOWED_HOSTS = [DOMAIN]

CSRF_TRUSTED_ORIGINS = [DOMAIN]

SECURE_BROWSER_XSS_FILTER = config("SECURE_BROWSER_XSS_FILTER", cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config("SECURE_CONTENT_TYPE_NOSNIFF", cast=bool)

SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS")
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)

SESSION_COOKIE_AGE = config("SESSION_COOKIE_AGE", default=1209600)
SESSION_COOKIE_HTTPONLY = config("SESSION_COOKIE_HTTPONLY", default=True, cast=bool)
SESSION_COOKIE_NAME = config("SESSION_COOKIE_NAME", default="sessionid")
SESSION_COOKIE_SAMESITE = config("SESSION_COOKIE_SAMESITE", default="Lax")
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)

CSRF_USE_SESSIONS = config("CSRF_USE_SESSIONS", default=True, cast=bool)
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static_src')]
STATIC_ROOT = "../vol/static"

MEDIA_URL = "media/"    
MEDIA_ROOT = "../vol/media"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("CACHE_LOCATION"),
        "OPTIONS": {
            "pool_class": "redis.BlockingConnectionPool",
        },
        "KEY_PREFIX": "cms_cache",
    }
}
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 900