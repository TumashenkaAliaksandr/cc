from django.contrib.sitemaps.views import sitemap
from django.urls import path

from sitemap import StaticViewSitemap
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import robots_txt

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('success/', views.success, name='success'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),


]



# Добавляем маршруты для медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
