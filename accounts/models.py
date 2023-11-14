from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
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

    def get_number_of_participated_books(self):
        return self.book_translators.filter(status='translated').count()

    def get_number_of_translated_pages(self):
        return self.page_translator.filter(is_reviewed=True).count()

    def get_average_translation_accuracy(self):
        translated_pages = self.page_translator.filter(is_reviewed=True)
        total_accuracy = sum(page.translation_accuracy for page in translated_pages) if translated_pages else 0

        average_accuracy = total_accuracy / translated_pages.count() if translated_pages.count() > 0 else 0
        return round(average_accuracy * 10, 2)

