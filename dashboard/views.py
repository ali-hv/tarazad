from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts.forms import CustomPasswordChangeForm
from books.models import Book, Page
from django.http import Http404


@login_required
def dashboard(request):
    books = Book.objects.filter(status='in-progress', translators=request.user)
    context = {'books': books, }
    return render(request, 'dashboard/index.html', context=context)


@login_required
def profile(request):
    form = CustomPasswordChangeForm(request.user)
    return render(request, 'dashboard/profile.html', {'form': form})


@login_required
def book_pages(request, book_id):
    pages = Page.objects.filter(translator=request.user, book_id=book_id)
    context = {'pages': pages}
    return render(request, 'dashboard/book_pages.html', context=context)


@login_required
def translate_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if page.translator != request.user or page.is_translated:
        raise Http404

    context = {'page': page}
    return render(request, 'dashboard/translate_page.html', context=context)
