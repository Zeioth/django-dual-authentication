# django-dual-authentication

This module allows authentication with either a username or an email address. It overrides [Django] authenticate method, so it's backwards incompatibility proof.

## Installation

Add this line to your settings.py

    AUTHENTICATION_BACKENDS = ['django-dual-authentication.models.DualAuthentication']

Now it's working. Quick and painless, right?
