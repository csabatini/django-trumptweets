import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# not tests, just Django settings
SECRET_KEY = 'test'
INSTALLED_APPS = (
    'trumptweets',
    'django.contrib.staticfiles',
)
ROOT_URLCONF = 'trumptweets.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MIDDLEWARE_CLASSES = ()
