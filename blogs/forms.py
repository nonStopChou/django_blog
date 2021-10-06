from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
       
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner', 'date']