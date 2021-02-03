from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home),
    path('accounts', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)