from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import MarketplaceUser
from django.contrib.auth.admin import UserAdmin


@admin.register(MarketplaceUser)
class MarketplaceUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'tariff', 'balance')
    fieldsets = UserAdmin.fieldsets + (
        (_('Services'), {'fields': ('tariff', 'balance')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
