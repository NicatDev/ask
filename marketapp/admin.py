from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from marketapp.models import Blog,Category,Tag,Services,Psychology,Message,Partners,Faq,Training,Team

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
    # exclude = ('content_without_ck','content','name','bottomcontent','sidename','sidecontent','bottomname')
    
    
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog,MyModelAdmin)
admin.site.register(Services,MyModelAdmin)

admin.site.register(Psychology,MyModelAdmin)
admin.site.register(Message)
admin.site.register(Partners)
admin.site.register(Faq)
admin.site.register(Training)
admin.site.register(Team)
