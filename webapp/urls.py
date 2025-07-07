
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.company, name='company'),
    path('success/', views.success, name='success'),

]



# Добавляем маршруты для медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
