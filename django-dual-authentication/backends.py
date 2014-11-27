from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class DualAuthentication(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.

    """
    def authenticate(self, username=None, password=None):
        try:
            kwargs = {'username': username}
            user = get_user_model().objects.get(**kwargs)
        except:
            kwargs = {'email': username}
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
            