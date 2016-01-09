from django.contrib import admin
from .models import Ticket, Comment
from .forms import CommentAdminForm


class CommentInline(admin.StackedInline):
    model = Comment
    form = CommentAdminForm
    extra = 1


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'user', 'subject', 'status']
    list_display_links = ['created_at', 'subject']
    readonly_fields = ['user', 'is_read_by_user', 'is_read_by_staff']
    inlines = [CommentInline]
    list_filter = ['status', 'is_read_by_staff']
