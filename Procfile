release: python back_end/server.py migrate
web: gunicorn gettingstarted.wsgi --log-file -
heroku ps:scale web=1
