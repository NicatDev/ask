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

def home(request):

    psychologies = Psychology.objects.all()
    services = Services.objects.all().order_by('ordering')
    if len(services)>6:
        services = services[0:6]
    blogs = Blog.objects.all().select_related('category').only('category','category__name','title','content_without_ck','mainimage','backimage')
    if len(blogs)>3:
        blogs = blogs[0:3]
    partners = Partners.objects.all()
    faq = Faq.objects.all()
    trainings = Training.objects.all()
    if len(trainings)>3:
        trainings = trainings[0:3]
    context = {
        'trainings':trainings,
        'partners':partners,
        'faq':faq,
        'blogs':blogs,
        'psychologies':psychologies,
        'services':services,

    }
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
    return render(request,'about.html',context)


def psychology(request):
    psychologies = Psychology.objects.all()
    context = {
        'psychologies':psychologies,
    }
    
    return render(request,'psychologies.html',context)

from django.shortcuts import get_object_or_404

def psychologySingle(request,slug):
    psychology = get_object_or_404(Psychology, slug=slug)
    context = {
        'psy':psychology
    }
    return render(request, 'psychologySingle.html',context)


def services(request):
    services = Services.objects.all()
    
    context = {
        'services':services,
    }
    
    return render(request,'services.html',context)

def serviceSingle(request,slug):
    service = get_object_or_404(Services, slug=slug)
    related_services =  Services.objects.all().only('name','icon','description_without_ck').exclude(id=service.id)

    if len(related_services) > 4:
        related_services = related_services[0:4]

    context = {
        'service':service,
        'related_services':related_services
    }

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
    
    return render(request,'blogs.html',context)


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
    if previous_blog:
        context['pre_blog']=previous_blog
        context['next_blog']=next_blog
    return render(request, 'blogSingle.html',context)

def contact(request):
    context = {}
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
        
    return render(request, 'trainingSingle.html',context)