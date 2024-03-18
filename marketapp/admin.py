from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from marketapp.models import Blog,TrainingSection,PsychologySection,Category,Tag,Services,Psychology,Message,Partners,Faq,Training,Show,Podcast,Team,ServiceSection,Photo,Video,Article,News,Event

class SideModelInline(admin.TabularInline):  
    model = ServiceSection

class MainModelAdmin(admin.ModelAdmin):
    inlines = [SideModelInline]

admin.site.register(Services, MainModelAdmin)

class PSideModelInline(admin.TabularInline):  
    model = PsychologySection

class PMainModelAdmin(admin.ModelAdmin):
    inlines = [PSideModelInline]

admin.site.register(Psychology,PMainModelAdmin)

class TSideModelInline(admin.TabularInline):  
    model = TrainingSection

class TMainModelAdmin(admin.ModelAdmin):
    inlines = [TSideModelInline]

admin.site.register(Training,TMainModelAdmin)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Article)

admin.site.register(Message)
admin.site.register(Partners)
admin.site.register(Faq)
admin.site.register(Team)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(News)
admin.site.register(Event)
admin.site.register(Show)
admin.site.register(Podcast)
