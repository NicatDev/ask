from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from marketapp.models import *
from django.urls import translate_url
from django.db.models import Q,F,FloatField,Count
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.conf import settings
import json
from marketapp.forms import Messageform

def events(request):
    events = Event.objects.all()
    paginator = Paginator(events, 4)
    page = request.GET.get("page", 1)
    events = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    recent_events = Event.objects.all()[::-1][:3]
    context = {
        'recent_events':recent_events,
        'events':events,
        'total_pages':total_pages
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'events.html',context)

def shows(request):
    events = Show.objects.all()
    paginator = Paginator(events, 4)
    page = request.GET.get("page", 1)
    events = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    recent_events = Show.objects.all()[::-1][:3]
    context = {
        'recent_events':recent_events,
        'events':events,
        'total_pages':total_pages
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'shows.html',context)

def podcasts(request):
    events = Podcast.objects.all()
    paginator = Paginator(events, 4)
    page = request.GET.get("page", 1)
    events = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    recent_events = Podcast.objects.all()[::-1][:3]
    context = {
        'recent_events':recent_events,
        'events':events,
        'total_pages':total_pages
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'podcasts.html',context)

def video(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 4)
    page = request.GET.get("page", 1)
    videos = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    context = {
        'videos':videos,
        'total_pages':total_pages
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'videos.html',context)

def gallery(request):
    photos = Photo.objects.all()
    context = {
        'photos':photos
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'gallery.html',context)

def home(request):

    psychologies = Psychology.objects.all()
    services = Services.objects.all().order_by('ordering')
    if len(services)>6:
        services = services[0:6]
    blogs = Blog.objects.all().select_related('category')
    if len(blogs)>3:
        blogs = blogs[0:3]
    partners = Partners.objects.all()
    faq = Faq.objects.all()
    trainings = Training.objects.all()

    if len(trainings)>3:
        trainings = trainings[0:3]

    team = Team.objects.all()
    context = {
        'team':team,
        'trainings':trainings,
        'partners':partners,
        'faq':faq,
        'blogs':blogs,
        'psychologies':psychologies,
        'services':services,

    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'home.html',context)

def home2(request):
    psychologies = Psychology.objects.all()
    services = Services.objects.all().order_by('ordering')
    if len(services)>6:
        services = services[0:6]
    blogs = Blog.objects.all().select_related('category').only('category','category__name','title','content_without_ck','mainimage','backimage')
    if len(blogs)>3:
        blogs = blogs[0:3]
    context = {
        'blogs':blogs,
        'services':services,
        'psychologies':psychologies,
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'home2.html',context)


def about(request):
    psychologies = Psychology.objects.all()[0:5]
    services = Services.objects.all().order_by('ordering')[0:6]
    team = Team.objects.all()

    context = {
        "services":services,
        'team':team,
        'psychologies':psychologies,
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'about.html',context)


def psychology(request):
    psychologies = Psychology.objects.all()
    context = {
        'psychologies':psychologies,
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'psychologies.html',context)

from django.shortcuts import get_object_or_404

def psychologySingle(request,slug):
    psychology = get_object_or_404(Psychology, slug=slug)
    context = {
        'psy':psychology
    }
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    researchs = Services.objects.all()
    context['researchs'] = researchs
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'psychologySingle.html',context)


def services(request):
    services = Services.objects.all()
    
    context = {
        'services':services,
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'services.html',context)

def serviceSingle(request,slug):
    service = get_object_or_404(Services, slug=slug)
    related_services =  Services.objects.all().exclude(id=service.id)

    if len(related_services) > 4:
        related_services = related_services[0:4]

    context = {
        'service':service,
        'related_services':related_services
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'service-single.html',context)


def blogs(request):
    
    blog_list = Blog.objects.all().only('mainimage','title','content_without_ck','category__name')
    recent_blogs = Blog.objects.all()[:: -1]
    if len(recent_blogs)>3:
        recent_blogs = recent_blogs[0:3]
    categories = Category.objects.all().only('name','id')
    tags = Tag.objects.all()
    
    if request.GET.get('blog'):
        name = request.GET.get('blog')
        blog_list = blog_list.filter(Q(title__icontains=name) | Q(content_without_ck__icontains=name))
        
    if request.GET.get('category'):
        category = request.GET.get('category')
        blog_list = blog_list.filter(category__id=category)
    
    if request.GET.get('tag'):
        tag = request.GET.get('tag')
        blog_list = blog_list.filter(tag__id__in=tag)
        
    paginator = Paginator(blog_list, 4)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    
    context = {
        'blogs':blogs,
        'total_pages':total_pages,
        'categories':categories,
        'recent_blogs':recent_blogs,
        'tags':tags
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'blogs.html',context)

def articles(request):
    
    blog_list = Article.objects.all()
    recent_blogs = Article.objects.all()[:: -1]
    if len(recent_blogs)>3:
        recent_blogs = recent_blogs[0:3]
    categories = Category.objects.all().only('name','id')
    tags = Tag.objects.all()
    
    if request.GET.get('blog'):
        name = request.GET.get('blog')
        blog_list = blog_list.filter(Q(title__icontains=name) | Q(content_without_ck__icontains=name))
        
    if request.GET.get('category'):
        category = request.GET.get('category')
        blog_list = blog_list.filter(category__id=category)
    
    if request.GET.get('tag'):
        tag = request.GET.get('tag')
        blog_list = blog_list.filter(tag__id__in=tag)
        
    paginator = Paginator(blog_list, 4)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    
    context = {
        'blogs':blogs,
        'total_pages':total_pages,
        'categories':categories,
        'recent_blogs':recent_blogs,
        'tags':tags
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'articles.html',context)

def articleSingle(request,slug):
    blog = get_object_or_404(Article, slug=slug)
    related_blogs =  Article.objects.all().exclude(id=blog.id)
    categories = Category.objects.all().only('name','id')
    tags = Tag.objects.all()
    if len(related_blogs) > 3:
        related_blogs = related_blogs[0:3]

  

    next_blog = Article.objects.exclude(id=blog.id).first()
    if next_blog:
        previous_blog = Article.objects.exclude(id=blog.id).exclude(id=next_blog.id).order_by('-created_at').first()
    else:
        previous_blog = {}
    context = {
        'blog':blog,
        'recent_blogs':related_blogs,
        'categories':categories,
        'tags':tags
    }

    researchs = Services.objects.all()
    context['researchs'] = researchs
    if previous_blog:
        context['pre_blog']=previous_blog
        context['next_blog']=next_blog
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'articleSingle.html',context)

def blogSingle(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    related_blogs =  Blog.objects.all().exclude(id=blog.id)
    categories = Category.objects.all().only('name','id')
    tags = Tag.objects.all()
    if len(related_blogs) > 3:
        related_blogs = related_blogs[0:3]

  

    next_blog = Blog.objects.exclude(id=blog.id).first()
    if next_blog:
        previous_blog = Blog.objects.exclude(id=blog.id).exclude(id=next_blog.id).order_by('-created_at').first()
    else:
        previous_blog = {}
    context = {
        'blog':blog,
        'recent_blogs':related_blogs,
        'categories':categories,
        'tags':tags
    }

    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    if previous_blog:
        context['pre_blog']=previous_blog
        context['next_blog']=next_blog
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'blogSingle.html',context)

def contact(request):
    researchs = Services.objects.all()
    context = {
        'researchs':researchs
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'Contact.html',context)

def message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        newmessage = Messageform(data=data)
        if newmessage.is_valid():
            newmessage.save()
        else:
            return HttpResponse(status=405) 
        data = {'message': 'Data saved successfully'}
        return JsonResponse(data)
    else:
        return HttpResponse(status=405) 
    
    
def training(request):
    training_list = Training.objects.all()
    paginator = Paginator(training_list, 4)
    page = request.GET.get("page", 1)
    trainings = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    recent_trainings = Training.objects.all()[::-1]
    context = {
        'trainings':trainings,
        'total_pages':total_pages,
        "recent_trainings":recent_trainings
    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'trainings.html',context)


def trainingSingle(request,slug):
    training = get_object_or_404(Training, slug=slug)
    related_trainings =  Training.objects.all().exclude(id=training.id)
 
    if len(related_trainings) > 3:
        related_trainings = related_trainings[0:3]

  

    next_training = Training.objects.exclude(id=training.id).first()
    if next_training:
        previous_training = Training.objects.exclude(id=training.id).exclude(id=next_training.id).order_by('-created_at').first()
    else:
        previous_training = {}
    context = {
        'training':training,
        'recent_trainings':related_trainings,
    }
    if previous_training:
        context['pre_training']=previous_training
        context['next_training']=next_training
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request, 'trainingSingle.html',context)


def news(request):
    
    blog_list = News.objects.all()
    recent_blogs = News.objects.all()[:: -1]
 
        
    paginator = Paginator(blog_list, 4)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    
    context = {
        'news':blogs,
        'total_pages':total_pages,
        'recent_news':recent_blogs,

    }
    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    return render(request,'news.html',context)


def newsSingle(request,slug):
    blog = get_object_or_404(News, slug=slug)
    related_blogs =  News.objects.all().exclude(id=blog.id)

    if len(related_blogs) > 3:
        related_blogs = related_blogs[0:3]

  

    next_blog = News.objects.exclude(id=blog.id).first()
    if next_blog:
        previous_blog = News.objects.exclude(id=blog.id).exclude(id=next_blog.id).order_by('-created_at').first()
    else:
        previous_blog = {}
    context = {
        'blog':blog,
        'recent_blogs':related_blogs,
  
    }

    researchs = Services.objects.all()
    context['researchs'] = researchs
    pyschologies = Psychology.objects.all()
    context['pyschologies'] = pyschologies
    trainings = Training.objects.all()
    context['trainings'] = trainings
    if previous_blog:
        context['pre_blog']=previous_blog
        context['next_blog']=next_blog
    return render(request, 'newsSingle.html',context)