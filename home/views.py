from django.shortcuts import render


def home_page(request):
    return render(request, "home/index.html")


def about_us(request):
    return render(request, "home/about_us.html")


def contact_us(request):
    return render(request, "home/contact_us.html")
