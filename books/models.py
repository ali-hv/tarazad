from django.db import models
from core.models import TimeStampedModel
from core.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Book(TimeStampedModel):
    LANGUAGES = (
        ('en-us', 'English'),
        ('es-sp', 'Spanish'),
    )

    STATUS = (
        ('translated', 'Translated'),
        ('in-progress', 'In Progress'),
        ('not-started', 'Not Started')
    )

    name = models.CharField(max_length=255, verbose_name="Book's Name")
    detail = models.TextField(verbose_name="Book's Detail")
    file = models.FileField(upload_to="books/original/", verbose_name="Book's File")
    author = models.CharField(max_length=255, verbose_name="Book's Author")
    language = models.CharField(max_length=5, choices=LANGUAGES, verbose_name="Book's Language")
    pages_number = models.PositiveIntegerField(verbose_name="Book's Pages Number")
    publication_date = models.DateTimeField(verbose_name="Publication Date")
    translated_date = models.DateTimeField(blank=True, verbose_name="Translated Date")
    min_translators = models.PositiveIntegerField(verbose_name="Minimum Number of Translators to Start")
    status = models.CharField(max_length=11, choices=STATUS, verbose_name="Book's Status")
    translators = models.ManyToManyField(User, verbose_name="Book's Translators", related_name="book_translators")

