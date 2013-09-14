# -*- coding: utf-8 -*-
"""
    Settings.env_prod
    ~~~~~~~~~~~~~~

    Esse arquivo só é importado quando está rodando em produção em produção (prod)
    no heroku, ele identifica que está neste ambiente por conta de variaveis de ambiente.

    Quando estamos desenvolvendo em casa (dev) outro arquivo é carregado.

    :copyright: (c) 2013 by arruda.
"""

import dj_database_url

SITE_ID = 1

DEBUG = True
SERVE_MEDIA = False

# ver quem vai ser o servidor de midia =S
#MEDIA_SERVER_URL = 'http://rmr.arruda.blog.br'
# MEDIA_URL = MEDIA_SERVER_URL+'/media/'
# STATIC_URL = MEDIA_SERVER_URL+'/static/'

DATABASES = {
             'default': dj_database_url.config(default='postgres://localhost')
             }
