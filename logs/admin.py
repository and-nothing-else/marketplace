from django.contrib import admin
from .models import BalanceLog


@admin.register(BalanceLog)
class BalanceLogAdmin(admin.ModelAdmin):

    list_display = ['created_at', 'description', 'sum', 'user', 'operation_type']
    readonly_fields = ['created_at', 'description', 'sum', 'user', 'operation_type']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
