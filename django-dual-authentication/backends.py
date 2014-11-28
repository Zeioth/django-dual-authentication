from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.conf import settings

###################################
"""  DEFAULT SETTINGS + ALIAS   """
###################################


try:
    am = settings.AUTHENTICATION_METHOD
except:
    am = 'both'
try:
    cs = settings.AUTHENTICATION_CASE_SENSITIVE
except:
    cs = 'both'

#####################
"""   EXCEPTIONS  """
#####################


VALID_AM = ['username', 'email', 'both']
VALID_CS = ['username', 'email', 'both', 'none']

if (am not in VALID_AM):
    raise Exception("Invalid value for AUTHENTICATION_METHOD in project "
                    "settings. Use 'username','email', or 'both'.")

if (cs not in VALID_CS):
    raise Exception("Invalid value for AUTHENTICATION_CASE_SENSITIVE in project "
                    "settings. Use 'username','email', 'both' or 'none'.")

############################
"""  OVERRIDDEN METHODS  """
############################


class DualAuthentication(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    """

    def authenticate(self, username=None, password=None):
        try:
            if ((am == 'email') or (am == 'both')):
                if ((cs == 'email') or cs == 'both'):
                    kwargs = {'email': username}
                else:
                    kwargs = {'email__iexact': username}

                user = get_user_model().objects.get(**kwargs)
            else:
                raise
        except:
            if ((am == 'username') or (am == 'both')):
                if ((cs == 'username') or cs == 'both'):
                    kwargs = {'username': username}
                else:
                    kwargs = {'username__iexact': username}

                user = get_user_model().objects.get(**kwargs)
        finally:
            try:
                if user.check_password(password):
                    return user
            except:
                return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None
            