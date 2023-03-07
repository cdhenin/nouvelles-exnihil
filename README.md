# Nouvelles exnihil

This is the source code of the website [nouvelles.exnihil.fr](https://nouvelles.exnihil.fr/).

The site presents texts and novellas written by Florent Naud about a fictional futuristic universe.

![nouvelle exnihil image](style/img/og-image.png)

## Technical stack
* Postgresql
* Python Django
* Bulma CSS
* node-sass

### How to run (development)

#### With Docker, docker-compose and make

##### Installation 

```
$ make setenv ## Create and fill .env file for development
$ make start ## Launch project with postgres database, migration and django web server
$ make seed-local-db ## Fill db container with test data
```

##### Work on CSS

```
$ make css-watch ## Compile scss files with watch mode if you want to work on 
```

or 

```
$ make css-build ## Compile scss files
```

##### Deal with static files

```
$ make collectstatic ## Launch collectstatic command in the docker web container and copy static folder on the host machine 
```

#### Without Docker

##### Prerequites 
* postgresql with a db `nouvelles_exnihil`
* pipenv
* python 3.6
* psycopg2-binary 2.8.6
* node v16.17.0

##### Installation 

Run:

```
$ pipenv shell
$ pipenv install
```

Generate a value for DJANGO_SECRET_KEY:

```
$ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

and export the output as DJANGO_SECRET_KEY environment variable.

Then run:
```
$ python manage.py migrate
$ python manage.py runserver
```

- Set a .env file with 
```
DEBUG=True
POSTGRES_PASSWORD='<your postgres user>'
POSTGRES_USER='<your postgres user>'
ALLOWED_HOSTS='localhost'
``` 

and run 

 ```
$ export $(cat .env | xargs)
```

##### Launch webapp

- Launch django
```
$ python manage.py migrate
$ python manage.py runserver
```

##### Work on CSS

- Generate css from scss 
```
$ cd style
$ yarn install
$ yarn start
```

##### Deal with static files

- Regenerate static folder
```
$ python manage.py collectstatic --noinput --clear
```

