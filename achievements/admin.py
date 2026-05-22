from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Achievement


@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ('student_name', 'title', 'category', 'level', 'place', 'date', 'is_published')
    list_filter = ('category', 'level', 'is_published', 'date')
    list_editable = ('is_published',)
    search_fields = ('student_name_uz', 'title_uz', 'teacher_name_uz')
    date_hierarchy = 'date'



