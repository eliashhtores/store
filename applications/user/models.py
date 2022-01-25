from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def email(self):
        return self.email

    def get_full_name(self):
        return self.full_name
