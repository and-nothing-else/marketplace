from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from seo.admin import SEO_ADMIN_FIELDSET
from .models import Article


@admin.register(Article)
class ArticleAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'image', 'text', 'active')
        }),
        SEO_ADMIN_FIELDSET
    )
