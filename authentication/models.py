from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Username is required field.')
        if email is None:
            raise TypeError('Email is a required field.')
        

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):        
        if password is None:
            raise TypeError('Password cannot be None.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_student(self, username, email, password):
        if password is None:
            raise TypeError('Password cannot be None.')
        
        user = self.create_user(username, email, password)
        user.is_student = True
        user.save()
        return user

    def create_teacher(self, username, email, password):
        if password is None:
            raise TypeError('Password cannot be None.')

        user = self.create_user(username, email, password)
        user.is_teacher = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    contact_no = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return ''