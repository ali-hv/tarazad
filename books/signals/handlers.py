from django.shortcuts import get_object_or_404
from books.models import Book, InProgressBook
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Book)
def add_book_to_inprogressbooks(sender, instance: Book, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = Book.objects.get(id=instance.id)
        if previous.status != instance.status:
            if instance.status == "in-progress":
                book = InProgressBook.objects.create(book=instance)
            elif instance.status == "translated":
                book = get_object_or_404(InProgressBook, book=instance)
                book.delete()
