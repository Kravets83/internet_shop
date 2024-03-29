from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as gl
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                "Superuser is_staff=false")
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                "Superuser is_superuser=false")
        if kwargs.get('is_active') is not True:
            raise ValueError(
                "Superuser is_active=false")

        return self.create_user(email, user_name,  password, **kwargs)

    def create_user(self, email, user_name,  password, **kwargs):

        if not email:
            raise ValueError(gl('Enter email'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,**kwargs)

        user.set_password(password)
        user.save()
        return user

class BaseUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    email = models.EmailField(gl('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(gl('about'), max_length=500, blank=True)
    country = CountryField()
    phone_number = models.TextField(max_length=15, blank=True)
    postcode = models.CharField(max_length=150, blank=True)
    address_line1 = models.CharField(max_length=150, blank=True)
    address_line2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()





    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.user_name













