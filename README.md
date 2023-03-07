# Django static and media files deployment to GCP (Google Cloud Platform) with App Engine
As the extend of the initial project DjangoGCPAppEngine, this project is focusing to handle static and media files. If you want to know how to setup the configuration other than static and media files, please refer the detail in DjangoGCPAppEngine.

## Download JSON key to Google cloud
JSON key is required to allow Google App Engine get access to the Google Storage (Bucket)

To download the JSON Key, in the Google Cloud console, go to Menu menu > IAM & Admin > Service Accounts. Select your service account. Click Keys > Add key > Create new key. Select JSON, then click Create.

In this project, JSON Key located within DjangoGCPStaticFiles the same folder with wsgi.py, asgi.py, urls and env. 

Sample value of JSON Key is like this:

```py
{
  "type": "service_account",
  "project_id": "django-sample",
  "private_key_id": "40 characters unique id in here",
  "private_key": "-----BEGIN PRIVATE KEY-----\n very long character ----END PRIVATE KEY-----\n",
  "client_email": "django-cobaan@appspot.gserviceaccount.com",
  "client_id": "21 digit number in here",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/django-sample%40appspot.gserviceaccount.com"
}
```

## Static and Media Configuration
The configuration for Google Storage in the production.py within settings folder:
```py
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "django-cobaan-bucket"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    BASE_DIR, "bucket_cred.json"
)

GS_PROJECT_ID = "django-sample"
GS_STATIC_BUCKET_NAME = "django-sample-bucket"
GS_MEDIA_BUCKET_NAME = "django-sample-bucket"  # same as STATIC BUCKET if using single bucket both for static and media

STATIC_URL = "https://storage.googleapis.com/{}/static/".format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = "https://storage.googleapis.com/{}/media/".format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"

UPLOAD_ROOT = "media/uploads/"

DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"
```

## Running the project in development environment
To run development environment, you need to use the following command:
``` sh
  python manage.py runserver --settings=DjangoGCPStaticFiles.settings.development
```