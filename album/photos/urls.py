from django.urls import path

from photos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category=<str:slug>', views.category_list, name='category_list'),
    path('search/', views.search_result, name='search'),
    path('photos/<int:pk>/', views.post_detail, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)