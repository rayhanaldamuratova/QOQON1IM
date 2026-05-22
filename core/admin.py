from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import SchoolInfo


@admin.register(SchoolInfo)
class SchoolInfoAdmin(TranslationAdmin):
    fieldsets = (
        ("Asosiy ma'lumotlar", {
            'fields': ('name', 'tagline', 'description', 'founded_year')
        }),
        ("Statistika", {
            'fields': ('student_count', 'teacher_count')
        }),
        ("Aloqa", {
            'fields': ('address', 'phone', 'email', 'map_embed_url')
        }),
        ("Media", {
            'fields': ('logo', 'hero_image')
        }),
    )



