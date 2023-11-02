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
    publication_date = models.IntegerField(verbose_name="Publication Date")
    translated_date = models.DateTimeField(blank=True, null=True, verbose_name="Translated Date")
    min_translators = models.PositiveIntegerField(verbose_name="Minimum Number of Translators to Start")
    status = models.CharField(max_length=11, choices=STATUS, verbose_name="Book's Status")
    translators = models.ManyToManyField(User, blank=True, verbose_name="Book's Translators",
                                         related_name="book_translators")

    def __str__(self):
        return self.name


class InProgressBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="in_progress_book", verbose_name="Book")
    pages_left = models.PositiveIntegerField(verbose_name="Pages Left")
    extra_notes = models.TextField(blank=True, null=True, verbose_name="Extra Notes")

    def save(self, *args, **kwargs):
        if not self.pages_left:
            self.pages_left = self.book.pages_number

        super(InProgressBook, self).save(*args, **kwargs)


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_pages", verbose_name="Book")
    file = models.FileField(upload_to="books/pages/", verbose_name="Page's File")
    translated_content = models.TextField(blank=True, null=True, verbose_name="Translated Content")
    translator = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True,
                                      related_name="page_translator", verbose_name="Page's Translator")
