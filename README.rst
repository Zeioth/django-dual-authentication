`Django-dual-authentication <https://github.com/Zeioth/django-dual-authentication/>`__
==========================
.. image:: https://api.travis-ci.org/Zeioth/django-dual-authentication.svg
    :target: https://travis-ci.org/Zeioth/django-dual-authentication/builds
    
.. image:: https://img.shields.io/pypi/v/django-dual-authentication.svg
    :target:  https://pypi.python.org/pypi/django-dual-authentication/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://github.com/Zeioth/django-dual-authentication/blob/master/LICENSE

This package allows to authenticate a user with either a username an
email address, or both. It overrides
`Django <https://www.djangoproject.com/>`__ authenticate method, so it
should work in almost any case of use, without touch anything else.

Supported versions:

-  Python >= 2.7
-  Django >= 1.5

Installation
------------

Run::

    pip install django-dual-authentication

Then, add this line to your settings.py::

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.backends.DualAuthentication']

Quick and painless, right?

Settings
--------

-  ``AUTHENTICATION_METHOD``: You can authenticate your users by
   ``'username'``, ``'email'``, ``'both'``. Default: ``'both'``.
-  ``AUTHENTICATION_CASE_SENSITIVE``: You can choose ``'username'``,
   ``'email'``, ``'both'``, ``'none'``. Default: ``'username'``.

Common issues
-------------

We've been reported about users having problems with MySQL and
dual-authentication case sensitive option. This is because `mysql is
case-insensitive by
default <https://docs.djangoproject.com/en/1.7/ref/databases/#collation-settings>`__.
So, if you need case sensitive authentication, probably you'd prefer
avoid this database engine.

Also, note that if you combine certain options like
``AUTHENTICATION_METHOD = 'username'`` and
``AUTHENTICATION_CASE_SENSITIVE = 'username'``, then might be a good
idea check if a not case sensitive user already exists, for your
registation form's username field. Other way, users having the same
username with different capital letters, will not be able to login, for
obvious reasons.

Testing
-------

-  Clone this repository.
-  Open testproject directory.
-  Run syncdb or migrate depending your django version, and runserver.
-  Open http://localhost:8000/admin/ and try to login.

Updates
-----------

-  Dec 2014: Stable release
-  Dec 2015: All it's working fine. No changes.
-  Dec 2016: All it's working fine. No changes.
-  Dec 2017: All it's working fine. No changes.
-  Dec 2018: All it's working fine. No changes.
-  Apr 2019: Added support for django 2.0+ and Python ~3.7.

