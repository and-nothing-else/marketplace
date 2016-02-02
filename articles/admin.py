from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Article


@admin.register(Article)
class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title']
