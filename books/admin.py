from django.contrib import admin
from books.models import Book, InProgressBook, Page


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'pages_number', 'min_translators', 'get_number_of_translators']


@admin.register(InProgressBook)
class InProgressBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'pages_left', ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['book', 'translator', ]
