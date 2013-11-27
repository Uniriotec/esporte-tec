#!/bin/sh

heroku pg:reset DATABASE_URL --app esporte-tec
heroku run python manage.py syncdb --noinput --app esporte-tec
heroku run python manage.py loaddata esporte_tec/fixtures/auth_user.yaml --app esporte-tec
heroku run python manage.py loaddata esporte_tec/fixtures/sites.yaml --app esporte-tec
