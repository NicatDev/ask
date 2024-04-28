from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from marketapp.models import Subscriber,Testimonials,Student,TrainingItems,Vacancy,TrainingSection,PsychologySection,Category,Tag,Services,Psychology,Message,Partners,Training,Show,Team,ServiceSection,Article,News

class SideModelInline(admin.StackedInline):  
    model = ServiceSection
    exclude = ['title','description']

    extra = 0


class MainModelAdmin(admin.ModelAdmin):
    inlines = [SideModelInline]
    exclude = ['name','description','title']

admin.site.register(Services, MainModelAdmin)

class PSideModelInline(admin.StackedInline):  
    model = PsychologySection
    exclude = ['bottomDescription','title','description']

    extra = 0


class PMainModelAdmin(admin.ModelAdmin):
    inlines = [PSideModelInline]
    exclude = ['name','description','title']
    

admin.site.register(Psychology,PMainModelAdmin)

class TSideModelInline(admin.StackedInline):  
    model = TrainingSection
    exclude = ['title','description']

    extra = 0


class TMainModelAdmin(admin.ModelAdmin):
    inlines = [TSideModelInline]
    exclude = ['name','description','title']


admin.site.register(Training,TMainModelAdmin)

admin.site.register(Category)
admin.site.register(Tag)

class ArticleModelAdmin(admin.ModelAdmin):
    exclude = ['content','title','content_2']

admin.site.register(Article,ArticleModelAdmin)

admin.site.register(Message)
admin.site.register(Partners)

admin.site.register(Team)

class NewsShowModelAdmin(admin.ModelAdmin):
    exclude = ['content','title']

admin.site.register(News,NewsShowModelAdmin)
admin.site.register(Show,NewsShowModelAdmin)

admin.site.register(Vacancy)
admin.site.register(TrainingItems)
admin.site.register(Student)
admin.site.register(Testimonials)
admin.site.register(Subscriber)