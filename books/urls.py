from django.urls import path
from .views import books_list

app_name = "books"

urlpatterns = [
    path('list/', books_list, name='books_list')
]
