from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('2',home2,name='home2'),
    path('gallery',gallery,name='gallery'),
    path('videos',video,name='videos'),
    path('eventler',events,name='events'),
    path('verlisler',shows,name='shows'),
    path('podkastlar',podcasts,name='podcasts'),
    path('haqqımızda',about,name='about'),
    path('biznespsixologiyasi',psychology,name='psychology'),
    path('biznespsixologiyasi/<slug>',psychologySingle,name='psychologySingle'),
    path('blog/<slug>',blogSingle,name='blogSingle'),
    path('tedqiqatlar',services,name='services'),
    path('tedqiqatlar/<slug>',serviceSingle,name='serviceSingle'),
    path('bloqlar',blogs,name='blogs'),
    path('meqaleler',articles,name='articles'),
    path('telimler',training,name='training'),
    path('telimler/<slug>',trainingSingle,name='trainingSingle'),
    path('bloqlar/<slug>',blogSingle,name='blogSingle'),
    path('meqaleler/<slug>',articleSingle,name='articleSingle'),
    path('elaqe',contact,name='contact'),
    path('message',message,name='message'),
    path('xeberler',news,name='news'),
    path('xeberler/<slug>',newsSingle,name='newsSingle'),
]