from django.urls import path
from .views import dashboard, book_pages, translate_page

app_name = "dashboard"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:book_id>', book_pages, name='book_pages'),
    path('translate/<int:page_id>', translate_page, name='translate_page'),
]
