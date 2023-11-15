from django.core.validators import MaxValueValidator
from core.settings import AUTH_USER_MODEL
from books.models import Book, Page
from django.db import models

User = AUTH_USER_MODEL


class Translator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_translator")
    translation_accuracy = models.PositiveIntegerField(validators=[MaxValueValidator(100)], default=0)
    books_participated = models.PositiveIntegerField(default=0)
    pages_translated = models.PositiveIntegerField(default=0)
