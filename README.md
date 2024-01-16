# ROCHE-_TASK-




## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/pavansai26/.git
$ cd project_folder
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
# Perform migrations and apply to the database
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

In order to test it please test it in postman.
