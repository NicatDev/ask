from marketapp.sitemap import ArticleSiteMap,TrainingSiteMap,TagSiteMap,ServiceSitemap, StaticSitemap
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
# from marketapp.sitemap import BlogSiteMap,ServiceSitemap, StaticSitemap
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns


sitemaps = {
    'tag_sitemap': TagSiteMap,
    'training_sitemap': TrainingSiteMap,
    'article_sitemap': ArticleSiteMap,
    'service_sitemap': ServiceSitemap,
    'static_sitemap': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),

]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('', include("marketapp.urls")),
    
)



urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

