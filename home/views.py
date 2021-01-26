from django.shortcuts import render
from django.http import HttpResponse
from myblog.settings import EMAIL_HOST_USER
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages
from codersonly.models import blogPost
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request, 'home/home.html', {})


def contact(request):
    if request.method == 'POST':
        subject = request.POST['name']
        email = request.POST['email']
        message = request.POST['content']
        phone = request.POST['phone']
        if len(subject) < 2 or len(email) < 3 or len(phone) < 10 or len(message) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            messages.success(request, 'We Will Contact You Soon......')
            contac = Contact(Name=subject, email=email,
                             phone=phone, content=message)
            contac.save()
            send_mail(subject, message + phone + 'email of user ' + email, EMAIL_HOST_USER,
                      ['iamwebdeveloper77@gmail.com'])
    return render(request, 'home/contact.html', {})


def about(request):
    return HttpResponse('this is About Page')


def search(request):
    query = request.GET['query']
    if query == '':
        result = blogPost.objects.none()
    if len(query) > 78:
        result = blogPost.objects.none()
    else:
        resultauthor = blogPost.objects.filter(author__icontains=query)
        resulttitle = blogPost.objects.filter(title__icontains=query)
        resultcontent = blogPost.objects.filter(content__icontains=query)
        result = resulttitle.union(resultcontent, resultauthor)
    if result.count() == 0:
        messages.error(
            request, "No search results found. Please refine your query.")
    context = {'result': result, 'query': query}
    return render(request, 'home/search.html', context)

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        pass1 = request.POST['password']
        cpassword = request.POST['cpassword']
        user2 = User.objects.create_user(name,email,pass1)
        user2.first_name = firstname
        user2.last_name = lastname
        user2.save()
        messages.success(request,'Your Account Has Been Created')
        return redirect('home')


def loginuser(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       if username == '' :
           messages.error(request,'Please Fill Username Field')
           return redirect('home')
       if password == '':
           messages.error(request,"Please Fill Out The Password Field")
           return redirect('home')
       user1 = authenticate(username=username,password=password)
       if user1 is not None:
           login(request,user1)
           messages.success(request,'YOU ARE LOGGED IN NOW!!!!!!')
           return redirect('home')
   else:
        return redirect('home')

def logoutuser(request):
    logout(request)
    return redirect('home')