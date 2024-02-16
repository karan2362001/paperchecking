from django.shortcuts import render

def adminHomepage(request):
    return render(request,"adminHomepage.html")