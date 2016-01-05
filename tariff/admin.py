from django.contrib import admin
from .models import Tariff


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ['name', 'goods', 'price', 'is_recommended', 'ordering']
    list_editable = ['ordering']
