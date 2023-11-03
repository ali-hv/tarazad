from django.shortcuts import get_object_or_404


def export_book(Page, InProgressBook, book):
    pages = Page.objects.filter(book=book)
    text = ''
    for i in pages:
        text += f'{i.translated_content}\n'

    with open('book.txt', 'w') as f:
        f.write(text)

    obj = get_object_or_404(InProgressBook, book=book)
    obj.delete()
