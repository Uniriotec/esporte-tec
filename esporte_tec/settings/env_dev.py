# -*- coding: utf-8 -*-
"""
    Settings.env_dev
    ~~~~~~~~~~~~~~

    Esse arquivo só é importado quando estamos desenvolvendo (dev)
    em casa em nossos computadores.
    No heroku ele identifica que está em produção (prod) e carrega outro arquivo.

    :copyright: (c) 2013 by arruda.
"""

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


