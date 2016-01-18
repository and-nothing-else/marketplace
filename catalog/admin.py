from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from sorl.thumbnail.admin import AdminImageMixin
from .models import Category, Item, ItemPhoto


@admin.register(Category)
class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    list_display = ['name', 'slug', 'sku_allowed']
    list_editable = ['slug', 'sku_allowed']


class ItemPhotoInline(AdminImageMixin, admin.TabularInline):
    model = ItemPhoto


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'price']
    inlines = [ItemPhotoInline]
