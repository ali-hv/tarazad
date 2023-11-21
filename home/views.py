from translators.models import Translator
from django.shortcuts import render
from books.models import Book


def home_page(request):
    books = Book.objects.all()
    return render(request, "home/index.html", {'books': books})


def support(requests):
    return render(requests, "home/support.html")


def about_us(request):
    return render(request, "home/about_us.html")


def contact_us(request):
    return render(request, "home/contact_us.html")


def translators_list(request):
    translators = Translator.objects.all().order_by("-translation_accuracy", "-books_participated", "-pages_translated")
    return render(request, "home/translators_list.html", {"translators": translators})
