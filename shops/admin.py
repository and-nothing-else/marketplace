from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from seo.admin import SEO_ADMIN_FIELDSET
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['region']
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'owner', 'description', 'active')
        }),
        (_('contact'), {
            'fields': ('region', 'address', 'map_point', 'phone')
        }),
        SEO_ADMIN_FIELDSET
    )
