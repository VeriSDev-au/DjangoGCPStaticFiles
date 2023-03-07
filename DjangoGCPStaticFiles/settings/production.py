import os
from .base import *
from decouple import config
from google.oauth2 import service_account

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": config("PROD_DB_ENGINE"),
        "HOST": config("PROD_DB_HOST"),
        "NAME": config("PROD_DB_NAME"),
        "USER": config("PROD_DB_USERNAME"),
        "PASSWORD": config("PROD_DB_PASSWORD"),
    }
}

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "django-cobaan-bucket"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    BASE_DIR, "bucket_cred.json"
)

GS_PROJECT_ID = "django-cobaan"
GS_STATIC_BUCKET_NAME = "django-cobaan-bucket"
GS_MEDIA_BUCKET_NAME = "django-cobaan-bucket"  # same as STATIC BUCKET if using single bucket both for static and media

STATIC_URL = "https://storage.googleapis.com/{}/static/".format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = "https://storage.googleapis.com/{}/media/".format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"

UPLOAD_ROOT = "media/uploads/"

DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"
