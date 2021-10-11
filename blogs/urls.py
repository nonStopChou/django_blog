from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', HomeView, name='homeNoLogin'),
    path('home/<str:username>', HomeView, name='homeLogin'),
    path('home/<str:username>/addPost', AddpostView, name='addPost'),
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('posts/', PostView, name='posts'),
    path('logout/', LogoutView, name='logout'),
    path('editProfile/<str:username>', EdittingProfileView, name='editProfile'),
    path('deletePost/<str:username>/<int:post_id>', DeletePostView, name='deletePost'),
    path('posts/likepost/', LikePostView, name='likepost'),
    path('posts/searchCategory/likepost/', LikePostView, name='likepost'),
    path('allPosts/likepost/', LikePostView, name='likepost'),
    path('posts/searchCategory/', SearchCategoryView, name='searchCategory'),
    path('lobby/', UserListView, name='userList'),
    path('viewProfile/<str:username>', ViewProfileView, name='viewProfile'),
    path('allPosts/', AllPostsView, name='allPosts'),
    path('music/', MusicView, name='music'),
    path('covid19/', CovidView, name='covid19'),
]
