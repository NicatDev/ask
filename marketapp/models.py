from django.db import models
from django.contrib.auth import get_user, get_user_model
from marketapp.utils import *
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError

URL_CHOICES = [
        ('home', 'home'),
        ('articles', 'articles'),
        ('services', 'services'),
        ('contact', 'contact'),
        ('training', 'training'),
    ]

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now=True,blank=True,null=True,)
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_alt = models.CharField(max_length=1200,null=True,blank=True)
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True


class MetaInfo(models.Model):
    page_name = models.CharField(max_length=300, choices=URL_CHOICES, unique=True)
    meta_title = models.CharField(max_length=10,null=True,blank=True,verbose_name='title for seo')
    meta_description = models.CharField(max_length=300,null=True,blank=True,verbose_name='Meta Description')
    meta_keyword = models.CharField(max_length=300,null=True,blank=True,verbose_name='keywords for seo')
    image_alt = models.CharField(max_length=300,null=True,blank=True)


    def __str__(self):
        return self.page_name
    
    def delete(self, *args, **kwargs):
        raise ValidationError("Meta məlumatları silinə bilməz!")
    
        
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
        # Azerbaycan Dili (az)
        if self.name_az:
            new_slug_az = seo(self.name_az)
            self.slug_az = new_slug_az
            if Services.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while Services.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.name_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.name_en:
            new_slug_en = seo(self.name_en)
            self.slug_en = new_slug_en
            if Services.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while Services.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.name_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.name_ru:
            new_slug_ru = seo(self.name_ru)
            self.slug_ru = new_slug_ru
            if Services.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while Services.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.name_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

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
    
class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

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
        # Azerbaycan Dili (az)
        if self.name_az:
            new_slug_az = seo(self.name_az)
            self.slug_az = new_slug_az
            if Psychology.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while Psychology.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.name_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.name_en:
            new_slug_en = seo(self.name_en)
            self.slug_en = new_slug_en
            if Psychology.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while Psychology.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.name_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.name_ru:
            new_slug_ru = seo(self.name_ru)
            self.slug_ru = new_slug_ru
            if Psychology.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while Psychology.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.name_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

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
    description = models.TextField(null=True,blank=True)
    image = models.ImageField()
    field = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return '--'+self.full_name  
    
class Partners(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField()
    href = models.CharField(max_length=800)
    
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
    
    def get_absolute_url(self):
        return reverse('trainingSingle', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # Azerbaycan Dili (az)
        if self.name_az:
            new_slug_az = seo(self.name_az)
            self.slug_az = new_slug_az
            if Training.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while Training.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.name_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.name_en:
            new_slug_en = seo(self.name_en)
            self.slug_en = new_slug_en
            if Training.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while Training.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.name_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.name_ru:
            new_slug_ru = seo(self.name_ru)
            self.slug_ru = new_slug_ru
            if Training.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while Training.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.name_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

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
        # Azerbaycan Dili (az)
        if self.title_az:
            new_slug_az = seo(self.title_az)
            self.slug_az = new_slug_az
            if Article.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while Article.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.title_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.title_en:
            new_slug_en = seo(self.title_en)
            self.slug_en = new_slug_en
            if Article.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while Article.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.title_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.title_ru:
            new_slug_ru = seo(self.title_ru)
            self.slug_ru = new_slug_ru
            if Article.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while Article.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.title_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

        super(Article, self).save(*args, **kwargs)
            
    def get_absolute_url(self):
        return reverse('articleSingle', kwargs={"slug": self.slug})
    

class News(BaseMixin):
    title = models.CharField(max_length = 300)
    image = models.ImageField()
    content = models.TextField()
    date = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'-{self.title}'
    
    def save(self, *args, **kwargs):
        # Azerbaycan Dili (az)
        if self.title_az:
            new_slug_az = seo(self.title_az)
            self.slug_az = new_slug_az
            if News.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while News.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.title_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.title_en:
            new_slug_en = seo(self.title_en)
            self.slug_en = new_slug_en
            if News.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while News.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.title_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.title_ru:
            new_slug_ru = seo(self.title_ru)
            self.slug_ru = new_slug_ru
            if News.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while News.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.title_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

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
        if self.title_az:
            new_slug_az = seo(self.title_az)
            self.slug_az = new_slug_az
            if Show.objects.filter(slug_az=new_slug_az).exists():
                count_az = 0
                while Show.objects.filter(slug_az=new_slug_az).exists():
                    new_slug_az = f"{seo(self.title_az)}-{count_az}"
                    count_az += 1
                self.slug_az = new_slug_az

        # İngilizce (en)
        if self.title_en:
            new_slug_en = seo(self.title_en)
            self.slug_en = new_slug_en
            if Show.objects.filter(slug_en=new_slug_en).exists():
                count_en = 0
                while Show.objects.filter(slug_en=new_slug_en).exists():
                    new_slug_en = f"{seo(self.title_en)}-{count_en}"
                    count_en += 1
                self.slug_en = new_slug_en

        # Rusça (ru)
        if self.title_ru:
            new_slug_ru = seo(self.title_ru)
            self.slug_ru = new_slug_ru
            if Show.objects.filter(slug_ru=new_slug_ru).exists():
                count_ru = 0
                while Show.objects.filter(slug_ru=new_slug_ru).exists():
                    new_slug_ru = f"{seo(self.title_ru)}-{count_ru}"
                    count_ru += 1
                self.slug_ru = new_slug_ru

        super(Show, self).save(*args, **kwargs)

