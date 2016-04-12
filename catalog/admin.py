from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from sorl.thumbnail.admin import AdminImageMixin
from seo.admin import SEO_ADMIN_FIELDSET
from .models import Category, Item, ItemPhoto


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    list_display = ['name', 'slug', 'sku_allowed']
    list_editable = ['slug', 'sku_allowed']
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'sku_allowed', 'size_set')
        }),
        (_('Tree position'), {
            'fields': ('_position', '_ref_node_id')
        }),
        (_('Filters'), {
            'fields': ('filter_price_allowed', 'filter_color_allowed', 'filter_size_allowed', 'filter_fabric_allowed',),
            'classes': ('collapse',)
        }),
        SEO_ADMIN_FIELDSET
    )


class ItemPhotoInline(AdminImageMixin, admin.TabularInline):
    model = ItemPhoto


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'price', 'active', 'disabled']
    inlines = [ItemPhotoInline]
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'article', 'price', 'old_price', 'description')
        }),
        (_('owner'), {
            'fields': ('shop',),
        }),
        (_('properties'), {
            'fields': ('color', 'size', 'standard_size', 'fabric'),
            'classes': ('collapse',)
        }),
        (_('display parameters'), {
            'fields': ('created_at', 'updated_at', 'active', 'disabled'),
            'classes': ('collapse',)
        }),
        SEO_ADMIN_FIELDSET
    )
