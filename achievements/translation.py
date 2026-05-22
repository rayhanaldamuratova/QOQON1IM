from modeltranslation.translator import register, TranslationOptions
from .models import Achievement


@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('student_name', 'title', 'description', 'teacher_name')



