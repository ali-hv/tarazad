from django.shortcuts import get_object_or_404
from books.models import Book, InProgressBook, Page
from django.db.models.signals import pre_save
from django.dispatch import receiver
import PyPDF2


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

                book = InProgressBook.objects.create(book=instance)
                translators = instance.translators.all()
                number_of_translators = translators.count()
                pages_number = instance.pages_number
                number_of_pages_for_each_translator = int(pages_number/number_of_translators)
                for i, j in enumerate(range(1, pages_number+1, number_of_pages_for_each_translator)):
                    for page in range(j, number_of_pages_for_each_translator + j):
                        page_text = pdf_reader.pages[page-1].extract_text()
                        page = Page(book=instance, page=page, original_content=page_text, translator=translators[i])
                        page.save()

            elif instance.status == "translated":
                book = get_object_or_404(InProgressBook, book=instance)
                book.delete()
