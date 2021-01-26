from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Bloghome'),
    path('<str:slug>', views.blogPosts, name='Blogposts'),
]
