from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               
    path('about/', views.about, name='about'),         
    path('blog/', views.blog_home, name='blog_home'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]