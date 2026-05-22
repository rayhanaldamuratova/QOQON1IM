from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import StaffMember


@admin.register(StaffMember)
class StaffMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'role', 'position', 'subject', 'experience_years', 'order', 'is_active')
    list_filter = ('role', 'subject', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('full_name_uz', 'full_name_ru', 'position_uz')

    fieldsets = (
        ("Shaxsiy ma'lumotlar", {
            'fields': ('full_name', 'photo', 'role', 'position', 'subject')
        }),
        ("Qo'shimcha", {
            'fields': ('bio', 'education', 'experience_years')
        }),
        ("Aloqa", {
            'fields': ('email', 'phone')
        }),
        ("Sozlamalar", {
            'fields': ('order', 'is_active')
        }),
    )



