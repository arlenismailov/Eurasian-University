from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(AboutUniversity)
class AboutUniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AboutCollege)
class AboutCollegeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Lyceum)
class LyceumTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Structure)
class StructureTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Recruitment)
class RecruitmentTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(OtherLinks)
class EventTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(News)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
