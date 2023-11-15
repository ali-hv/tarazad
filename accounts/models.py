from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    identity_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static("home/images/icons/default-avatar.png")

    def get_full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
