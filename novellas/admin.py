from django.contrib import admin
from .models import Tag, Novella

# Register your models here.

class NovellaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Novella, NovellaAdmin)
