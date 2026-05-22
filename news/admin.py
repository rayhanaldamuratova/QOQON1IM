from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, NewsCategory


@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')
    list_filter = ('is_published', 'category', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title_uz', 'title_ru', 'title_en')
    date_hierarchy = 'created_at'



