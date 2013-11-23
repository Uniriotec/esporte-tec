
"""
    Settings.installed_apps
    ~~~~~~~~~~~~~~

    aqui possui apenas a lista de apps instaladas

    :copyright: (c) 2013 by arruda.
"""

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'mptt',
    'esporte_tec.areas',
    'esporte_tec.membros',
    'esporte_tec.noticias',
    'esporte_tec.startups',
)
