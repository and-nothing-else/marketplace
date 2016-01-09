from django.contrib import admin
from .models import Help


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'ordering']
    list_editable = ['ordering']
