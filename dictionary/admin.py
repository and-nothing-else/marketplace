from django.contrib import admin
from .models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_default']
    filter_horizontal = ('region',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


class SizeInline(admin.TabularInline):
    model = Size


@admin.register(SizeSet)
class SizeSetAdmin(admin.ModelAdmin):
    inlines = [SizeInline]
