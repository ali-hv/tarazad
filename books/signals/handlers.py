from django.shortcuts import get_object_or_404
from books.models import Book, InProgressBook, Page
from django.db.models.signals import pre_save
from django.dispatch import receiver
import PyPDF2

from books.scripts.export_book import export_book


@receiver(pre_save, sender=Book)
def add_book_to_inprogressbooks(sender, instance: Book, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = Book.objects.get(id=instance.id)
        if previous.status != instance.status:
            if instance.status == "in-progress":
                pdf_file = open(instance.file.path, 'rb')
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                InProgressBook.objects.create(book=instance)

                translators = instance.translators.all()
                number_of_translators = translators.count()
                pages_number = instance.pages_number

                # Calculate the pages per translator and remainder
                pages_per_translator = pages_number // number_of_translators
                remainder = pages_number % number_of_translators

                start_page = 1

                for i, translator in enumerate(translators):
                    # Calculate the number of pages for the current translator
                    if i < remainder:
                        pages_for_translator = pages_per_translator + 1
                    else:
                        pages_for_translator = pages_per_translator

                    for page in range(start_page, start_page + pages_for_translator):
                        page_text = pdf_reader.pages[page - 1].extract_text()
                        page_instance = Page(book=instance, page=page, original_content=page_text,
                                             translator=translator)
                        page_instance.save()

                    start_page += pages_for_translator

            elif instance.status == "translated":
                book = get_object_or_404(InProgressBook, book=instance)
                book.delete()


@receiver(pre_save, sender=Page)
def decrease_pages_left(sender, instance: Page, **kwargs):
    if instance.id is None:
        pass
    else:
        previous = get_object_or_404(Page, id=instance.id)
        if previous.is_reviewed != instance.is_reviewed:
            if instance.is_reviewed:
                obj = get_object_or_404(InProgressBook, book=instance.book)
                if obj.pages_left == 1:
                    export_book(Page=Page, InProgressBook=InProgressBook, book=instance.book)
                else:
                    obj.pages_left -= 1
                    obj.save()
