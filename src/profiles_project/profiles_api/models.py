from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps django work with our custom user model."""

    def createUser(self, email, name, password):
        """creates a new user profile object."""

        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def createSuperUser(self, email, name, password):
        """creates a new super user profile object."""

        user = self.createUser(email, name, password)
        user.is_superuser = True
        user.is_staff = False

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def getFullName(self):
        """used to get a users full name."""
        return self.name

    def getShortName(self):
        """used to get a users short name."""
        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        return self.email
