from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorators import *
# Create your views here.

@login_required(login_url='login')
def home_view(request):
    obj = blog.objects.all()
    profile = Profile.objects.all()
    context = {
        'list': obj,
        'profile' : profile,
    }

    return render(request, 'blog.html', context)

@login_required(login_url='login')
def blogDetail_view(request, pk):
    blogDetail = blog.objects.get(id=pk)

    context = {
        'blog': blogDetail,
    }

    return render(request, 'blogDetail.html', context)

@unauthenticated_user
def register_view(request):
    register_form = createUserForm()
    if request.method == 'POST':
        register_form = createUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, 'An account is created for ' + user)
            return redirect('login')

    context = {
        'register_form': register_form,
    }
    return render(request, 'SignUp.html', context)

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return redirect('login')
    return render(request, "SignIn.html", {})

@login_required(login_url='login')
def logOut_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile_view(request):
    user = request.user.profile
    form = profileinfo(instance=user)
    if request.method == "POST":
        form = profileinfo(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {
        'form' : form,
    }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def create_blog_view(request):
    user = request.user.profile
    blogForm = profileinfo(instance=user)
    if request.method == "POST":
        blogForm = profileinfo(request.POST,request.FILES,instance=user)
        if blogForm.is_valid():
            blogForm.save()
    context = {
        'blogForm' : blogForm,
    }
    return render(request,'createBlog.html',context)