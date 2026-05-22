from modeltranslation.translator import register, TranslationOptions
from .models import StaffMember


@register(StaffMember)
class StaffMemberTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'bio', 'education')



