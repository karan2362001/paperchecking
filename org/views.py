from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages 
from api.models import CustomUser
import requests

def adminHomepage(request):
    return render(request,"adminHomepage.html")

def addEmployee(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        role='3'
        url="http://127.0.0.1:8000/api/admin/"
        data={"username":username,"password":password,"role":role}
        response = requests.post(url,data)
        
        #Checking the status code of the response to see if it was successful or not
        if response.status_code==201:
            messages.success(request,'Employee added successfully!')
            return redirect('addEmployee')
        else:
            messages.error(request,'Error adding employee! Please try again later.')

    return render(request,"addEmployee.html")

def forms(request):
    return render(request,"forms.html")