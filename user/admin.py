from django.contrib import admin
from .models import MarketplaceUser
from django.contrib.auth.admin import UserAdmin


@admin.register(MarketplaceUser)
class MarketplaceUserAdmin(UserAdmin):
    pass
