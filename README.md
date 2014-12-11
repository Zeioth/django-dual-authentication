# django-dual-authentication
This package allows to authenticate a user with either a username an email address, or both. It overrides [Django](https://www.djangoproject.com/) authenticate method, so it should work in almost any case of use, without touch anything else.

Supported versions:

 * Python >= 2.7
 * Django >= 1.5

## Installation
Run

    pip install django-dual-authentication

Then, add this line to your settings.py

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.backends.DualAuthentication']

Quick and painless, right?

## Settings

* ``AUTHENTICATION_METHOD``: You can authenticate your users by ``'username'``, ``'email'``, ``'both'``. Default: ``'both'``.
* ``AUTHENTICATION_CASE_SENSITIVE``: You can choose ``'username'``, ``'email'``, ``'both'``, ``'none'``. Default: ``'both'``.

Please note that if you combine certain options like ``AUTHENTICATION_METHOD = 'username'`` and ``AUTHENTICATION_CASE_SENSITIVE = 'none'``, then might be a good idea check if a not case sensitive user already exists, for your registation form's username field. Other way, users having the same username with different capital letters, will not be able to login, for obvious reasons.

## Common issues
We've been reported about users having problems with MySQL and dual-authentication case sensitive option. This is because [mysql is case-insensitive by default](https://docs.djangoproject.com/en/1.7/ref/databases/#collation-settings). So, if you need case sensitive authentication, probably you'd prefer avoid this database engine.

## Testing
 * Clone this repository.
 * Open testproject directory.
 * Run syncdb or migrate depending your django version, and runserver.
 * Open http://localhost:8000/admin/ and try to login.
