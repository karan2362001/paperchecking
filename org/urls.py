from django.urls import path
from . import views

urlpatterns = [
    path("adminHomepage/",views.adminHomepage,name="adminHomepage"),
    path("addEmployee/",views.addEmployee, name='addEmployee'),  # Add a new
    path("adminHomepage/forms/",views.forms, name='forms'),
    
]