from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import SuperBanner


@admin.register(SuperBanner)
class SuperBannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title', 'image', 'ordering']
    list_display_links = ['image', 'title']
    list_editable = ['ordering']
