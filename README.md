# django-dual-authentication
This package allows to authenticate a user with either a username or an email address. It overrides [Django](https://www.djangoproject.com/) authenticate method, so it should work in almost any case of use, without touch anything else.

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

You can define them in your project settings.

* ``AUTHENTICATION_METHOD``: You can choose to authenticate your users by ``'username'``, ``'email'``, or ``'both'``. Default: ``'both'``.
* ``AUTHENTICATION_CASE_SENSITIVE``: I don't recommend to use this option, but it's a requisite of some projects. You can choose ``'username'``, ``'email'``, ``'both'``, ``'none'``. Default: ``'both'``.

Please note that if you combine certain options like ``AUTHENTICATION_METHOD = 'username'`` and ``AUTHENTICATION_CASE_SENSITIVE = 'none'``, then might be a good idea to use lower() in your registation form's username field. Other way, users having the same username with different capital letters, will not be able to login, for obvious reasons.

## Testing
 * Clone this repository.
 * Open testproject directory.
 * Run syncdb or migrate depending your django version, and runserver.
 * Open http://localhost:8000/admin/ and try to login.
