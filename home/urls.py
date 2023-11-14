from django.urls import path
from .views import home_page, support, about_us, contact_us, translators_list

app_name = "home"

urlpatterns = [
    path("", home_page, name="home_page"),
    path("support", support, name="support"),
    path("about-us", about_us, name="about_us"),
    path("contact-us", contact_us, name="contact_us"),
    path("translators-list", translators_list, name="translators_list"),
]