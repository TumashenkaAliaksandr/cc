from django.contrib.sitemaps.views import sitemap
from django.urls import path

from sitemap import StaticViewSitemap
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import robots_txt, find_pros

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path("cart/", views.cart_view, name="cart"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('company/', views.company, name='company'),
    path('success/', views.success, name='success'),
    path('api/find-pros/', find_pros, name='find-pros'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),

]

# Добавляем маршруты для медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
