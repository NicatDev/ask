from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from marketapp.models import Blog,Category,Tag,Services,Psychology,Message,Partners,Faq,Training,Team,ServiceSection

class SideModelInline(admin.TabularInline):  # veya admin.StackedInline
    model = ServiceSection

class MainModelAdmin(admin.ModelAdmin):
    inlines = [SideModelInline]

admin.site.register(Services, MainModelAdmin)
    
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Psychology)
admin.site.register(Message)
admin.site.register(Partners)
admin.site.register(Faq)
admin.site.register(Training)
admin.site.register(Team)
