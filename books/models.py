from django.db import models
from django.contrib import admin
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
    cover_image = models.ImageField(upload_to='books/cover/', verbose_name="Book's Cover Image")
    original_file = models.FileField(upload_to="books/original/", verbose_name="Book's File")
    translated_md_file = models.FileField(upload_to="books/translated/markdown/", blank=True, null=True,
                                          verbose_name="Book's Translated MD File")
    translated_pdf_file = models.FileField(upload_to="books/translated/pdf/", blank=True, null=True,
                                           verbose_name="Book's Translated PDF File")
    author = models.CharField(max_length=255, verbose_name="Book's Author")
    language = models.CharField(max_length=5, choices=LANGUAGES, verbose_name="Book's Language")
    pages_number = models.PositiveIntegerField(verbose_name="Book's Pages Number")
    publication_date = models.IntegerField(verbose_name="Publication Date")
    translated_date = models.DateTimeField(blank=True, null=True, verbose_name="Translated Date")
    translating_date = models.DateTimeField(verbose_name="Translating Date")
    min_translators = models.PositiveIntegerField(verbose_name="Minimum Number of Translators to Start")
    status = models.CharField(max_length=11, choices=STATUS, verbose_name="Book's Status")
    translators = models.ManyToManyField(User, blank=True, verbose_name="Book's Translators",
                                         related_name="book_translators")

    def __str__(self):
        return self.name

    @admin.display(description="Number of Translators")
    def get_number_of_translators(self):
        book = Book.objects.get(id=self.id)
        return book.translators.all().count()


class InProgressBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="in_progress_book", verbose_name="Book")
    pages_left = models.PositiveIntegerField(verbose_name="Pages Left", blank=True, null=True)
    extra_notes = models.TextField(blank=True, null=True, verbose_name="Extra Notes")

    class Meta:
        verbose_name = "In Progress Book"

    def save(self, *args, **kwargs):
        if not self.pages_left:
            self.pages_left = self.book.pages_number

        super(InProgressBook, self).save(*args, **kwargs)


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_pages", verbose_name="Book")
    page = models.PositiveIntegerField()
    original_content = models.TextField(verbose_name="Original Content")
    translated_content = models.TextField(blank=True, null=True, verbose_name="Translated Content")
    is_translated = models.BooleanField(default=False)
    is_reviewed = models.BooleanField(default=False)
    translator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="page_translator",
                                   verbose_name="Page's Translator")
