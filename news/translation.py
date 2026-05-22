from modeltranslation.translator import register, TranslationOptions
from .models import News, NewsCategory


@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



