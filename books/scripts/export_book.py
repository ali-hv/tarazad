from django.shortcuts import get_object_or_404
from books.models import Book, Page
from django.core.files import File
import os.path


def export_book(book):
    pages = Page.objects.filter(book=book)
    text = ''

    for i in pages:
        text += f'{i.translated_content}\n'

    file_name = f'media/books/translated/tmp/{book.name}.md'

    with open(file_name, 'w') as f:
        f.write(text)

    obj = get_object_or_404(Book, id=book.id)

    with open(file_name, 'rb') as file:
        django_file = File(file)
        obj.translated_md_file.save(os.path.basename(file_name), django_file)

    obj.status = 'translated'

    obj.save()
