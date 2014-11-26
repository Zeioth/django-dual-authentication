# django-dual-authentication

This package allows [Django](https://www.djangoproject.com/) to authenticate a user with either a username or an email address. It overrides [Django](https://www.djangoproject.com/) authenticate method, so it should work in almost any case of use, without touch anything else.

Supported Python versions:

 * Python 2.7
 * Python 3.4

## Installation

Install it running

    pip install git+git://github.com/zeioth/django-dual-authentication.git@master

And add this line to your settings.py

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.models.DualAuthentication']

Quick and painless, right?

## Testing
 * Clone this repository.
 * Open testproject directory.
 * Run syncdb or migrate depending your django version, and runserver.
 * Open http://localhost:8000/admin/ and try to login.
