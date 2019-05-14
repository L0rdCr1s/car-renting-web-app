from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from time import strftime, gmtime
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError


class CustomManager(BaseUserManager):
    def _create_user(self, email=None, password=None, is_superuser=False, is_staff=False, is_active=False):
        if email is None:
            raise ValueError("users must have an email")
        if password is None:
            raise ValueError("users must have a password")

        user = self.model(
            email=self.normalize_email(email),
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **kwargs):
        user = self._create_user(
            email, password, is_staff=False, is_superuser=False, is_active=False)
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.date_joined = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        user.save(using=self._db)
        return user

    def create_staffuser(self, email=None, password=None, **kwargs):
        user = self._create_user(
            email, password, is_staff=True, is_superuser=False, is_active=False)
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.date_joined = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self._create_user(
            email, password, is_superuser=True, is_staff=True, is_active=True)
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.date_joined = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    users = CustomManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.last_name

    def get_username(self):
        return self.email


class UserProfile(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile_contact = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()

    # number of cars a user has ever booked
    booked_cars = models.IntegerField(default=0)

    # number of cars a user owns/registered as his in the system
    owned_cars = models.IntegerField(default=0)

    profiles = models.Manager()

    def __str__(self):
        return self.user.email