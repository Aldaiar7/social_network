from django.contrib.auth.models import BaseUserManager
from django.forms import ValidationError


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(
        self,
        email,
        username,
        password,
        phone,
        date_birth,
        first_name,
        second_name,
        *args,
        **kwargs
    ):
        """Create a new user profile"""

        if not email:
            raise ValueError("User must have email address")
        if not phone:
            raise ValueError("User must have phone number")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            phone=phone,
            date_birth=date_birth,
            first_name=first_name,
            second_name=second_name,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, email, username, password, phone, date_birth, first_name, second_name
    ):
        """Creating new superuser with credentials"""

        user = self.create_user(
            email, username, password, phone, date_birth, first_name, second_name
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
