from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),
]
 