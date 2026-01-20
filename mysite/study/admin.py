from django.contrib import admin
from .models import Card, Set

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ['name', 'card_amount']
    list_filter = ['name', 'card_amount']
    ordering = ['name']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'set']
    ordering = ['answer']