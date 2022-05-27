from django.contrib.auth.models import BaseUserManager



class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, password, *args, **kwargs):
        """Create a new user profile"""

        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email,
                        username=username,
                        phone=kwargs.get('phone'),
                        date_birth=kwargs.get('date_birth'),
                        first_name=kwargs.get('first_name'),
                        second_name=kwargs.get('second_name') )

        user.set_password(password)
        user.save(using=self._db)


        return user
    
    def create_superuser(self, email, username, password):
        """Creating new superuser with credentials"""

        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user