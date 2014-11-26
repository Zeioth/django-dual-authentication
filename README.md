# django-dual-authentication

This module allows authentication with either a username or an email address. It overrides [Django] authenticate method, so it's backwards incompatibility proof.

## Installation

Open your settings.py add this line:

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.models.DualAuthentication']

Quick and painless, right?
