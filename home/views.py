from translators.models import Translator
from django.shortcuts import render


def home_page(request):
    return render(request, "home/index.html")


def support(requests):
    return render(requests, "home/support.html")


def about_us(request):
    return render(request, "home/about_us.html")


def contact_us(request):
    return render(request, "home/contact_us.html")


def translators_list(request):
    translators = Translator.objects.all().order_by("-translation_accuracy", "-books_participated", "-pages_translated")
    return render(request, "home/translators_list.html", {"translators": translators})
