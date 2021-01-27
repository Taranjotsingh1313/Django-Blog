from django.shortcuts import render
from django.http import HttpResponse
from .models import blogPost
from .models import BlogComment
from django.shortcuts import redirect
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

def postcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = blogPost.objects.get(sno=postSno)
        blogComment = BlogComment(comment=comment,user=user,post=post)
        blogComment.save()
        return redirect('Bloghome')