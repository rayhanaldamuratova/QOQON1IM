from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'phone', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    search_fields = ('full_name', 'subject', 'message')
    readonly_fields = ('full_name', 'email', 'phone', 'subject', 'message', 'created_at')



