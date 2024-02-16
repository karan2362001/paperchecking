from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages 
from api.models import CustomUser
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

def adminHomepage(request):
    return render(request,"adminHomepage.html")

def facultyHomepage(request):
    return render(request,"FacultyHomePage.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(request,username=username,password=password)
        userData = get_object_or_404(CustomUser, username=username)
        userRole=userData.role
        if user is not None:
            if userRole==2:
                login(request,user)
                return redirect('adminHomepage')
            elif userRole==3:
                login(request,user)
                return redirect('facultyHomepage')
            else:
                messages.error(request,'Invalid Credentials! Please try again with correct credentials.')
                return redirect('login')

        else:
            messages.info(request,"invalid credentials...")
            return redirect('login')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return render(request,"login.html")