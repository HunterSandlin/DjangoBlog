from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<slug:slug>', views.article_detail),
    path('', views.article_list, name='article list'),
]
