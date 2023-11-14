from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404

from decorators import identity_verified_required
from .models import Book, Page


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


@identity_verified_required
@login_required
def add_translator(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.status == 'not-started':
        if request.user not in book.translators.all():
            if book.can_accept_new_translators():
                book.translators.add(request.user)
                messages.success(request, 'شما با موفقیت به مترجمان این کتاب اضافه شدید. لطفا در زمان مشخص شده با مراجعه به داشبورد، صفحات مشخص شده را ترجمه کنید')
            else:
                messages.warning(request, 'ظرفیت مترجمان این کتاب تکمیل شده است. می توانید در کتاب های بعدی مشارکت کنید')
        else:
            messages.warning(request, 'شما قبلا در ترجمه این کتاب عضو شده اید')
    else:
        messages.warning(request, 'زمان عضویت در ترجمه این کتاب به پایان رسیده است')

    return redirect('books:books_list')


def submit_translation(request):
    if request.method == "POST":
        data = dict(**request.POST)
        page_id = data['page_id'][0]
        translated_content = data['text'][0]
        page = get_object_or_404(Page, id=page_id)

        if request.user == page.translator and not page.is_translated:
            page.translated_content = translated_content
            page.is_translated = True
            page.save()
            return redirect('dashboard:book_pages', page.book.id)

        raise Http404
