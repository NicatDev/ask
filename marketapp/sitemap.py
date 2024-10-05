from django.contrib.sitemaps import Sitemap
from marketapp.models import *
from django.urls import reverse, NoReverseMatch
from django.utils.translation import get_language

class ArticleSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
    def location(self, obj: Article) -> str:
        lang = get_language()
        return f'/{lang}{obj.get_absolute_url()}'
    
class TrainingSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Training.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
    def location(self, obj: Training) -> str:
        lang = get_language()
        return f'/{lang}{obj.get_absolute_url()}'
    

class PsychologySiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Psychology.objects.all()

    def lastmod(self, obj):
        return obj.created_at
    
    def location(self, obj: Psychology) -> str:
        lang = get_language()
        return f'/{lang}{obj.get_absolute_url()}'


class TagSiteMap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'
    
    def items(self):
        return Tag.objects.all()

    def location(self,item):
        return reverse('home')
    
class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Services.objects.all()

    def location(self, obj: Services) -> str:
        lang = get_language()
        return f'/{lang}{obj.get_absolute_url()}'



class StaticSitemap(Sitemap):

    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'home', 'about', 'services',
            'blogs', 'portfolio',  'contact',
        ]

    def location(self, item):
        try:
            lang = get_language() 
            return f'/{lang}{reverse(item)}' 
        except NoReverseMatch:
            return f'/{get_language()}{reverse("home")}'

