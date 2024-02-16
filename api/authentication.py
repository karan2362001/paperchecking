# authentication.py

from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserAuthenticationBackend:

    def authenticate(self, request, email=None, password=None):
        User = get_user_model()
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
