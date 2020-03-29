from django.contrib import admin
from .models import LexiconItem

# Register your models here.

class LexiconItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'definition',)

admin.site.register(LexiconItem, LexiconItemAdmin)
