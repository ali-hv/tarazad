def export_book(Page, InProgressBook, book):
    pages = Page.objects.filter(book=book)
    text = ''
    for i in pages:
        text += f'{i.translated_content}\n'

    with open('book.txt', 'w') as f:
        f.write(text)

    obj = InProgressBook.objects.get(book=book)
    obj.delete()
    obj.save()
