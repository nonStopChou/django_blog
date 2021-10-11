from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from django.http import request
from .models import *
from .forms import *
# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from datetime import datetime
from django.core.paginator import Paginator
import pandas as pd
from django.templatetags.static import static


def HomeView(request, username=None):
    user = request.user
    if user is not None:
        username = user.username
    if request.method == "POST":
        user = User.objects.get(username=username)
        form = UserInfoForm(request.POST, request.FILES, instance=user.userinfo)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/blogs/home/'+username)
    if user.is_authenticated:
        info = UserInfo.objects.get(user=user)
        context = {
            "user" : user,
            'info' : info
        }
        return render(request, 'blogs/home.html', context=context)
    return render(request, 'blogs/home.html')
   
def PostView(request):
    user = request.user

    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.owner = request.user
            candidate.date = datetime.now()
            candidate.save()
            return redirect('posts')

    if user.is_authenticated:
        
        info = UserInfo.objects.get(user=user)
        posts = Post.objects.filter(owner=user)
        context = {
            'user' : user,
            'info' : info,    
            'posts' : posts,
            'likePost':info.likePost.all()
        }
        
        return render(request, 'blogs/posts.html', context= context)

    return render(request, 'blogs/posts.html')

def LoginView(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully for " + username + " !")
            return redirect('/blogs/home/'+username)
        messages.error(request, "Username or Password was wrong !")

    return render(request, 'blogs/login.html')

def LogoutView(request):
    logout(request)
    messages.success(request, "Logout Successfully !")
    return redirect('login')

def RegisterView(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pwd1 = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=pwd1)
            userinfo = UserInfo.objects.create(user=user)
            userinfo.email = form.cleaned_data.get('email')
            userinfo.save()
            messages.success(request, "Register Successfully for " + username + " !")
            return redirect('login')
        else:
            messages.error(request, form.errors)

    context = {
        'form' : form
    }
    return render(request, 'blogs/register.html', context)

def EdittingProfileView(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        form = UserInfoForm(instance=user.userinfo)
        context = {
            'user':user,
            'form':form 
        }
        return render(request, 'blogs/editProfile.html', context=context)
    return render(request, 'blogs/editProfile.html')

def AddpostView(request, username):
    
    user = request.user
    if user.is_authenticated:
        form = PostForm()
        context = {
            'user' : user, 
            'form' : form,
        }
    return render(request, 'blogs/addPost.html', context=context)

def DeletePostView(request, username, post_id):
    if request.user.username == username:
        obj = Post.objects.get(id=post_id)
        obj.delete()
    return redirect('posts')

def LikePostView(request):
    if request.method == "GET":
        postid = request.GET['post_id']
        obj = Post.objects.get(id=postid)
        user = request.user
        if user.is_authenticated:
            user_info = UserInfo.objects.get(user=user)
            if user_info.likePost.filter(id=postid).exists():
                user_info.likePost.remove(obj)
            else:
                user_info.likePost.add(obj)
        return HttpResponse('Success')
    return HttpResponse('Error')

def SearchCategoryView(request):
    
    user = request.user

    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.owner = request.user
            candidate.date = datetime.now()
            candidate.save()
            return redirect('posts')
    
    if user.is_authenticated:

        info = UserInfo.objects.get(user=user)
        category = request.GET.get('category')
        if category == 'All':
            posts = Post.objects.filter(owner=user)
        else:   
            posts = Post.objects.filter(owner=user).filter(category=category)
        context = {
            'user' : user,
            'info' : info,    
            'posts' : posts,
            'likePost':info.likePost.all()
        }
        
        return render(request, 'blogs/posts.html', context= context)

    return render(request, 'blogs/posts.html')

def UserListView(request):
    users = User.objects.all()
    context ={
        'users' : users
    }
    return render(request, 'blogs/lobby.html', context=context)

def ViewProfileView(request, username):

    user = User.objects.get(username = username)
    info = user.userinfo
    context = {
        'info' : info
    }
    return render(request, 'blogs/viewProfile.html', context=context)

def AllPostsView(request):
    
    posts = Post.objects.all()
    info = UserInfo.objects.get(user=request.user)

    context = {
        'posts' : posts,
        'likePost' : info.likePost.all(),
    }

    return render(request, 'blogs/allPosts.html', context = context)


def MusicView(request):
    paginator = Paginator(Music.objects.all(), 1)
    page = request.GET.get('page_num')
    page_obj = paginator.get_page(page)
    context = {
        'page_obj' : page_obj
    }
    return render(request, 'blogs/music.html', context=context)


def CovidView(request):

    # url = 'blogs/static/blogs/covid/Taiwan_covid.xlsx'
    url = static('/blogs/covid/Taiwan_covid.xlsx')
    df = pd.read_excel(url)
    print(df.head())
    print(url)
    return render(request, 'blogs/covid19.html')