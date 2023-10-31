from django.urls import path
from .views import home_page, about_us, contact_us

urlpatterns = [
    path("", home_page),
    path("about-us", about_us),
    path("contact-us", contact_us),
]