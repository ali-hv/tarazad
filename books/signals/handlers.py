from django.shortcuts import get_object_or_404
from books.models import Book, InProgressBook, Page
from django.db.models.signals import pre_save
from django.dispatch import receiver

from books.scripts.distribute_pages_to_translators import distribute
from books.scripts.export_book import export_book
from translators.models import Translator


@receiver(pre_save, sender=Book)
def add_book_to_inprogressbooks(sender, instance: Book, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = get_object_or_404(Book, id=instance.id)
        if previous.status != instance.status:
            if instance.status == "in-progress":
                distribute(instance)

            elif instance.status == "translated":
                for translator in instance.translators.all():
                    obj = get_object_or_404(Translator, user=translator)
                    obj.books_participated += 1
                    obj.save()

                in_progress_book = get_object_or_404(InProgressBook, book=instance)
                in_progress_book.delete()


@receiver(pre_save, sender=Page)
def decrease_pages_left(sender, instance: Page, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = get_object_or_404(Page, id=instance.id)
        if previous.is_reviewed != instance.is_reviewed:
            if instance.is_reviewed:
                translator = get_object_or_404(Translator, user=instance.translator)
                translator.pages_translated += 1
                translator.save()

                obj = get_object_or_404(InProgressBook, book=instance.book)
                if obj.pages_left == 1:
                    export_book(instance.book)
                else:
                    obj.pages_left -= 1
                    obj.save()
