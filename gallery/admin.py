from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import GalleryAlbum, GalleryPhoto


class GalleryPhotoInline(TranslationTabularInline):
    model = GalleryPhoto
    extra = 3
    fields = ('image', 'caption', 'order')


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(TranslationAdmin):
    list_display = ('title', 'photo_count', 'is_published', 'created_at')
    list_editable = ('is_published',)
    inlines = [GalleryPhotoInline]


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(TranslationAdmin):
    list_display = ('album', 'caption', 'order')
    list_filter = ('album',)



