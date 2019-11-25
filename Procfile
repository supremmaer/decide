release: python decide/manage.py migrate

web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'