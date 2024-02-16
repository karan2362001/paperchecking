from django.shortcuts import render

# Create your views here.
def FacultyHomePage(request):
    return render(request,FacultyHomePage.html)

def login(request):
    return render(request,login.html)

def logout(request):
    return render(request,logout.html)         