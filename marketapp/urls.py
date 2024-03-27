from django.urls import path,include
from .views import *

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
    path('',home,name='home'),
    path('2',home2,name='home2'),
    path('verlisler',shows,name='shows'),
    path('haqqımızda',about,name='about'),
    path('biznespsixologiyasi',psychology,name='psychology'),
    path('biznespsixologiyasi/<slug>',psychologySingle,name='psychologySingle'),
    path('tedqiqatlar',services,name='services'),
    path('tedqiqatlar/<slug>',serviceSingle,name='serviceSingle'),
    path('meqaleler',articles,name='articles'),
    path('telimler',training,name='training'),
    path('telimler/<slug>',trainingSingle,name='trainingSingle'),
    path('meqaleler/<slug>',articleSingle,name='articleSingle'),
    path('elaqe',contact,name='contact'),
    path('message',message,name='message'),
    path('submit_vacancy_form',submit_vacancy_form,name='submit_vacancy_form'),
    
    path('xeberler',news,name='news'),
    path('xeberler/<slug>',newsSingle,name='newsSingle'),
]