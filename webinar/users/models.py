from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model representing the users subscribed to the application."""

    class Meta:
        db_table = 'auth_user'
