# django-dual-authentication
This package allows to authenticate a user with either a username or an email address. It overrides [Django](https://www.djangoproject.com/) authenticate method, so it should work in almost any case of use, without touch anything else.

Supported versions:

 * Python 2.7 and 3.4
 * Django >= 1.5

## Installation
Run

    pip install django-dual-authentication

Then, add this line to your settings.py

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.backends.DualAuthentication']

Quick and painless, right?

## Testing
 * Clone this repository.
 * Open testproject directory.
 * Run syncdb or migrate depending your django version, and runserver.
 * Open http://localhost:8000/admin/ and try to login.
