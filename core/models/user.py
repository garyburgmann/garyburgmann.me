from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator


class CustomUser(AbstractUser):
    email = models.EmailField(
        error_messages={'unique': 'A user with that email already exists.'},
        help_text='Required. 254 characters or fewer.', max_length=254,
        unique=True, verbose_name='email address',
        validators=[EmailValidator])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
