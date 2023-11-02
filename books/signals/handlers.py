from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book


@receiver(post_save, sender=Book)
def add_book_to_inprogressbooks(sender, **kwargs):
    print(kwargs)
    