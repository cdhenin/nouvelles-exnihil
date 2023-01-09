# Nouvelles exnihil

Code source of https://nouvelles.exnihil.fr/

### Prerequites 
* postgresql with a db `nouvelles_exnihil`
* pipenv
* python 3.6
* psycopg2-binary 2.8.6


### Installation

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

### Development

- Regenerate static folder
```
$ python manage.py collectstatic --noinput --clear
```

- Generate css from scss 
```
$ cd style
$ yarn install
$ yarn start
```
