from django import forms
from .models import Message,Student
from django.contrib.auth.forms import UserCreationForm

class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name','subject','email','message']
    
        
    def __init__(self,*args,**kvargs):
        super(Messageform,self).__init__(*args,**kvargs)

class TrainingMessageForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
    
    def __init__(self,*args,**kvargs):
        super(TrainingMessageForm,self).__init__(*args,**kvargs)