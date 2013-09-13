from utils import LOCAL
import dj_database_url

SITE_ID = 1

DEBUG = False
SERVE_MEDIA = False

# ver quem vai ser o servidor de midia =S
#MEDIA_SERVER_URL = 'http://rmr.arruda.blog.br'
# MEDIA_URL = MEDIA_SERVER_URL+'/media/'
# STATIC_URL = MEDIA_SERVER_URL+'/static/'

DATABASES = {
             'default': dj_database_url.config(default='postgres://localhost')
             }
