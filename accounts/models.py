from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email_verified = models.BooleanField(default=False)
    phone_number = models.IntegerField(max_length=12)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
