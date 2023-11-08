from django.urls import path
from .views import books_list, add_translator, submit_translation

app_name = "books"

urlpatterns = [
    path('list/', books_list, name='books_list'),
    path('add_translator/<int:book_id>', add_translator, name='add_translator'),
    path('submit_translation/<int:page_id>', submit_translation, name='submit_translation'),
]
