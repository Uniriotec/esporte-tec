# -*- coding: utf-8 -*-
"""
    Settings
    ~~~~~~~~~~~~~~

    A divided settings module.

    :copyright: (c) 2013 by arruda.
"""

import os

from config import *
from installed_apps import *
from logging import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4@ttz@64por3hm190sa=kywq(#3cid_of$d9sz1s2pf6eujl)l'

ON_HEROKU = os.environ.has_key('DATABASE_URL')


NO_DEPRECATION_WARNINGS=False
if not ON_HEROKU:
    NO_DEPRECATION_WARNINGS=True
    from env_dev import *
else:
    from env_prod import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)

