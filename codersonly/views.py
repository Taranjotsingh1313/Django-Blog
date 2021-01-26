from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost
# Create your views here.


def home(request):
    allpsots = blogPost.objects.all()
    context = {'allposts': allpsots}
    return render(request, 'codersonly/bloghome.html', context)


def blogPosts(request, slug):
    id = slug
    allPosts = blogPost.objects.filter(slug=id).first()
    context = {'allPosts': allPosts}
    return render(request, 'codersonly/blogPosts.html', context)
