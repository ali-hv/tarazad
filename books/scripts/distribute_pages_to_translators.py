from books.models import InProgressBook, Page
from .edit import remove_page_top_section
import PyPDF2


def distribute(instance):
    pdf_file = open(instance.original_file.path, 'rb')
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
            page_text = remove_page_top_section(page_text)
            page_instance = Page(book=instance, page=page, original_content=page_text,
                                 translator=translator)
            page_instance.save()

        start_page += pages_for_translator
