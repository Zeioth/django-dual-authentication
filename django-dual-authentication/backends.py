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
    cs = 'username'

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
    
    if django.VERSION[0] == 1:
        def authenticate(self, username=None, password=None):
            return self._authenticate(username, password)
    else:
        def authenticate(self, request, username=None, password=None):
            return self._authenticate(username, password)
            
    def _authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        try:
            if ((am == 'email') or (am == 'both')):
                if ((cs == 'email') or cs == 'both'):
                    kwargs = {'email': username}
                else:
                    kwargs = {'email__iexact': username}

                user = UserModel.objects.get(**kwargs)
            else:
                raise
        except:
            if ((am == 'username') or (am == 'both')):
                if ((cs == 'username') or cs == 'both'):
                    kwargs = {'username': username}
                else:
                    kwargs = {'username__iexact': username}

                user = UserModel.objects.get(**kwargs)
        finally:
            try:
                if user.check_password(password):
                    return user
            except:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user.
                UserModel().set_password(password)
                return None

    def get_user(self, username):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=username)
        except UserModel.DoesNotExist:
            return None
