from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": config("DEV_DB_ENGINE"),
        "HOST": config("DEV_DB_IP"),
        "NAME": config("DEV_DB_NAME"),
        "USER": config("DEV_DB_USERNAME"),
        "PASSWORD": config("DEV_DB_PASSWORD"),
    }
}

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

STATIC_ROOT = "static/static/"
STATIC_URL = "/static/static/"

MEDIA_ROOT = "static/media"
MEDIA_URL = "/static/media/"

UPLOAD_ROOT = "uploads/"

DOWNLOAD_URL = "/static/media/downloads"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
