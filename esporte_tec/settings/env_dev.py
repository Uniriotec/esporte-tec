from utils import LOCAL

SITE_ID = 1
DEBUG = True
SERVE_MEDIA = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': LOCAL('db.sqlite') ,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


