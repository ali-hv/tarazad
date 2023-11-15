from django.contrib import admin

from translators.models import Translator


@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ["user", "books_participated", "pages_translated", "translation_accuracy"]
