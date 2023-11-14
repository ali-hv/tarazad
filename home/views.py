from django.db.models import Q, Count, Sum, Avg
from django.shortcuts import render
from accounts.models import User

def home_page(request):
    return render(request, "home/index.html")


def support(requests):
    return render(requests, "home/support.html")


def about_us(request):
    return render(request, "home/about_us.html")


def contact_us(request):
    return render(request, "home/contact_us.html")


def translators_list(request):
    users = User.objects.annotate(
        num_translated_books=Count('book_translators', filter=Q(book_translators__status='translated')),
        num_translated_pages=Sum('book_translators__book_pages__is_reviewed',
                                 filter=Q(page_translator__is_reviewed=True)),
        avg_translation_accuracy=Avg('page_translator__translation_accuracy',
                                     filter=Q(page_translator__is_reviewed=True))
    ).order_by('-num_translated_books', '-num_translated_pages', '-avg_translation_accuracy').filter(is_active=True)
    return render(request, "home/translators_list.html", {"users": users})
