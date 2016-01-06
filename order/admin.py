from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'sum', 'paymentType', 'paid']
    list_filter = ['paymentType', 'paid']
