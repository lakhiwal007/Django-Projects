from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class profileinfo(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class createBlogForm(ModelForm):
    class Meta:
        model = blog
        fields = '__all__'