from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def add_translator(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)

        if book.status == 'not-started':
            if request.user not in book.translators.all():
                book.translators.add(request.user)
                messages.success(request, 'شما با موفقیت به مترجمان این کتاب اضافه شدید. لطفا در زمان مشخض شده با مراجعه به داشبورد، صفحات مشخص شده را ترجمه کنید')
            else:
                messages.warning(request, 'شما قبلا در ترجمه این کتاب عضو شده اید')
        else:
            messages.warning(request, 'زمان عضویت در ترجمه این کتاب به پایان رسیده است')

        return redirect('books:books_list')
    else:
        return redirect('accounts:login')
