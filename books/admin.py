from books.models import Book, InProgressBook, Page
from django.utils.translation import ngettext
from django.contrib import admin, messages


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'pages_number', 'min_translators', 'get_number_of_translators']


@admin.register(InProgressBook)
class InProgressBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'pages_left', ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['book', 'page', 'translator', 'is_translated', 'is_reviewed', ]
    readonly_fields = ('original_content', )
    fields = ('book', 'page', 'original_content', 'translated_content', 'is_translated',
              'is_reviewed', 'translator', 'translation_accuracy', )
    list_filter = ['book__name', 'is_translated', 'is_reviewed', ]
    actions = ['make_reviewed']

    @admin.action(description='Mark selected pages as reviewed')
    def make_reviewed(self, request, queryset):
        updated = queryset.update(is_reviewed=True)
        message = f"{updated} page{(updated - 1) * 's'} was successfully marked as reviewed."
        self.message_user(request,
                          ngettext(
                              message, message, updated
                          ),
                          messages.SUCCESS)
