from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})

def aboutme_view(request):
    return render(request,'base/aboutme.html',{})

def campusinfo_view(request):
    return render(request,'base/Campus-info.html',{})

def studymaterial_view(request):
    return render(request,'base/Study Material.html',{})
## study material course
def institutecore_view(request):
    return render(request,'base/IC.html',{})

def HSS_view(request):
    return render(request,'base/HSS Courses.html',{})

def ESOs_view(request):
    return render(request,'base/ESO.html',{})

def studentcorner_view(request):
    return render(request,'base/Student Corner.html',{})