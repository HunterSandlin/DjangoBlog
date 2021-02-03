from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),
]

urlpatterns += staticfiles_urlpatterns()