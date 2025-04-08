from decouple import config
from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

DOMAIN = 'https://8000-idx-crm-1717074082797.cluster-bec2e4635ng44w7ed22sa22hes.cloudworkstations.dev'

ALLOWED_HOSTS = [DOMAIN, '127.0.0.1', 'localhost', "*"]

CSRF_TRUSTED_ORIGINS = [DOMAIN, 'http://127.0.0.1', 'http://localhost']

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

WHITENOISE_INDEX_FILE = True