Ghibli Movies is an exercise project for the job application to the sennder. It retries movie and people list from ghibli API and shows them within a Web UI.

# Install

```sh
apt install redis-server
pip install -r requirements.txt
python manage.py migrate
```

# Tasks

Synchronizes movie database with Redis in every 50 seconds.

```sh
python manage.py runworkers 
```

# Test

```sh
python manage.py test 
```

# Debug

```sh
python manage.py runserver 
```
