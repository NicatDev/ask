from django.db import models
from django.contrib.auth import get_user, get_user_model
from marketapp.utils import *
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now=True,blank=True,null=True,)
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_alt = models.CharField(max_length=1200,null=True,blank=True)
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True
        
class Vacancy(models.Model):
    name = models.CharField(max_length = 400)
    phone = models.CharField(max_length = 100)
    email = models.EmailField()
    birth = models.DateField()
    field = models.CharField(max_length = 700)
    cv = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name

class Services(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    title = models.CharField(max_length=200,null=True,blank=True)
    ordering = models.SmallIntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'-{self.name}'

    class Meta:
        verbose_name = "Research"
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Services.objects.filter(slug=new_slug).exists():
            count = 0
            while Services.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Services, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('serviceSingle', kwargs={"slug": self.slug})

class ServiceSection(models.Model):
    service = models.ForeignKey(Services,models.CASCADE,related_name="sections")
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'-{self.title}'

class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length = 120)
    def __str__(self):
        return self.name
    

            
    # def get_absolute_url(self):
    #     return reverse('blogSingle', kwargs={"slug": self.slug})
    

    


class Psychology(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    title = models.CharField(max_length=200,null=True,blank=True)
    ordering = models.SmallIntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'-{self.name}'

    class Meta:
        verbose_name = "Psychology"
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Psychology.objects.filter(slug=new_slug).exists():
            count = 0
            while Psychology.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Psychology, self).save(*args, **kwargs)
        
  
class PsychologySection(models.Model):
    psychology = models.ForeignKey(Psychology,models.CASCADE,related_name="psysections")
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField()
    bottomDescription = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'-{self.title}'
    


class Message(models.Model):
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Team(models.Model):
    full_name = models.CharField(max_length = 200)
    image = models.ImageField()
    field = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.full_name    
    
class Partners(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    full_name = models.CharField(max_length = 400)
    field = models.CharField(max_length = 400)
    company = models.CharField(max_length = 400)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField()
    file = models.FileField(null=True,blank=True)
    
    def __str__(self):
        return f'-{self.full_name}'

class Training(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    title = models.CharField(max_length=200,null=True,blank=True)
    ordering = models.SmallIntegerField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'-{self.name}'

    class Meta:
        verbose_name = "Training"
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Training.objects.filter(slug=new_slug).exists():
            count = 0
            while Training.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Training, self).save(*args, **kwargs)
        


class TrainingSection(models.Model):
    training = models.ForeignKey(Training,models.CASCADE,related_name="trainingsections")
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'-{self.title}'

class TrainingItems(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField(null=True,blank=True)
    training = models.ForeignKey(Training,on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    live = models.BooleanField(default=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'-{self.title}'

class Article(BaseMixin):
    title = models.CharField(max_length = 200)
    image = models.ImageField()
    content = models.TextField()
    content_2 = models.TextField()
    date = models.DateField(blank=True,null=True,)

    def __str__(self):
        return f'-{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = seo(self.title)
            
            if Article.objects.filter(slug=new_slug).exists():
                count = 2
                while Article.objects.filter(slug=new_slug).exists():
                    new_slug = f"{seo(self.title)}-{count}"
                    count += 1
            self.slug = new_slug
        super(Article, self).save(*args, **kwargs)
            
    def get_absolute_url(self):
        return reverse('blogSingle', kwargs={"slug": self.slug})
    

class News(BaseMixin):
    title = models.CharField(max_length = 300)
    image = models.ImageField()
    content = models.TextField()
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'-{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = seo(self.title)
            
            if News.objects.filter(slug=new_slug).exists():
                count = 2
                while News.objects.filter(slug=new_slug).exists():
                    new_slug = f"{seo(self.title)}-{count}"
                    count += 1
            self.slug = new_slug
        super(News, self).save(*args, **kwargs)
            
    def get_absolute_url(self):
        return reverse('blogSingle', kwargs={"slug": self.slug})

class Student(models.Model):
    name = models.CharField(max_length = 300)
    phone = models.CharField(max_length = 300)
    email = models.EmailField()
    training = models.CharField(max_length = 300)

    def __str__(self):
        return f'-{self.name}'
    
class Show(BaseMixin):
    title = models.CharField(max_length = 200)
    video = models.CharField(max_length = 3000,null=True,blank=True)
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return f'-{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = seo(self.title)
            
            if Show.objects.filter(slug=new_slug).exists():
                count = 2
                while Show.objects.filter(slug=new_slug).exists():
                    new_slug = f"{seo(self.title)}-{count}"
                    count += 1
            self.slug = new_slug
        super(Show, self).save(*args, **kwargs)

