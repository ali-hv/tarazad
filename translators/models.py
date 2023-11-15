from django.core.validators import MaxValueValidator
from core.settings import AUTH_USER_MODEL
from books.models import Book, Page
from django.db import models

User = AUTH_USER_MODEL


class Translator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_translator")
    translation_accuracy = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0)
    books_participated = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books_participated",
                                           blank=True, null=True)
    pages_translated = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="translator_pages",
                                         blank=True, null=True)
