web: gunicorn --chdir back_end server:app 
release: python back_end/server.py migrate
heroku ps:scale web=1
