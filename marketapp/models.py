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
        
    

class Services(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    title = models.CharField(max_length=200,null=True,blank=True)
    ordering = models.SmallIntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name

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
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length = 120)
    def __str__(self):
        return self.name
    
class Blog(BaseMixin):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length = 200)
    mainimage = models.ImageField()
    backimage = models.ImageField(null=True,blank=True)
    content = models.TextField()
    content_without_ck = models.CharField(max_length = 200)
    content_2 = models.TextField()
    content_without_ck_2 = models.CharField(max_length = 200)
    in_home = models.BooleanField(default=False)
    blog_date = models.DateField(blank=True,null=True,)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.title)
        self.slug = new_slug
        if Blog.objects.filter(slug=new_slug).exists():
            count = 0
            while Blog.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.title)}-{count}"
                count += 1
        super(Blog, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('blogSingle', kwargs={"slug": self.slug})
    

    
class Psychology(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    image = models.ImageField()
    second_image = models.ImageField(null=True,blank=True)
    second_description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Psychology.objects.filter(slug=new_slug).exists():
            count = 0
            while Psychology.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Psychology, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('psychologySingle', kwargs={"slug": self.slug})

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

class Faq(models.Model):
    question = models.CharField(max_length = 200)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    


class Training(BaseMixin):
    name = models.CharField(max_length = 800)
    description = models.TextField()
    description_without_ck = models.CharField(max_length = 200)
    image = models.ImageField(null=True,blank=True)
    bottomdescription = models.TextField()
    ordering = models.SmallIntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        new_slug = seo(self.name)
        self.slug = new_slug
        if Training.objects.filter(slug=new_slug).exists():
            count = 0
            while Training.objects.filter(slug=new_slug).exists():
                new_slug = f"{seo(self.name)}-{count}"
                count += 1
        super(Training, self).save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse('serviceSingle', kwargs={"slug": self.slug})
