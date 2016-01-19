from django.contrib import admin
from .models import Dictionary


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('item', 'translation')
    search_fields = ('item', 'translation')
