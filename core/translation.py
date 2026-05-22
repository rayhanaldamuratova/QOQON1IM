from modeltranslation.translator import register, TranslationOptions
from .models import SchoolInfo


@register(SchoolInfo)
class SchoolInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'tagline', 'description', 'address')



