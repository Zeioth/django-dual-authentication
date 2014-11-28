#########################################################
""" TEST settings for dual-authentication testproject """
#########################################################

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = '_'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['localhost']




###############################
""" APPLICATION DEFINITION  """
###############################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproject.urls'
TEMPLATE_DIRS = ((os.path.join(BASE_DIR, 'testproject/templates')),)
WSGI_APPLICATION = 'testproject.wsgi.application'
AUTHENTICATION_BACKENDS = ['testproject.dual-authentication.backends.DualAuthentication']



###############################
"""        DATABASE         """
###############################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




###############################
"""      STATIC MEDIA       """
###############################

STATIC_URL = '/static/'




###############################
"""   DUAL AUTHENTICATION  """
###############################

# Options: username, email, both
# Default: both
AUTHENTICATION_METHOD = 'both'

# Options: username, email, both, none
# Default: both
AUTHENTICATION_CASE_SENSITIVE = 'both'
