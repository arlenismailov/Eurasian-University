from django.contrib import admin
from .models import (
    AboutUniversity, AboutCollege, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, DSC, OtherLinks, Сontacts, Followus, Link, News, VerificationCode, Numberstudents, Lyceum
)

from modeltranslation.admin import TranslationAdmin


@admin.register(AboutUniversity)
class AboutUniversityAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("name", 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AboutCollege)
class AboutCollegeAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("name", 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Lyceum)
class LyceumAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("name", 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(VerificationCode)
admin.site.register(Numberstudents)


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    group_fieldsets = True
    inlines = [EventImageInline]
    list_display = ("title", "description")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Library)
admin.site.register(JobTitle)
admin.site.register(LanguageKnowledge)
admin.site.register(LaborActivity)
admin.site.register(Management)


@admin.register(Structure)
class StructureAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('description',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Recruitment)
class RecruitmentAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('title',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('title',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Direction)
admin.site.register(DSC)
admin.site.register(Сontacts)
admin.site.register(Followus)


@admin.register(OtherLinks)
class FollowusAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("title",)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Link)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("title", 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
