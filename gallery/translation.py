from modeltranslation.translator import register, TranslationOptions
from .models import GalleryAlbum, GalleryPhoto


@register(GalleryAlbum)
class GalleryAlbumTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(GalleryPhoto)
class GalleryPhotoTranslationOptions(TranslationOptions):
    fields = ('caption',)



