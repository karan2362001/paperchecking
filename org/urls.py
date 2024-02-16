from django.urls import path
from . import views

urlpatterns = [
    path("/adminHomepage/",views.adminHomepage,name="adminHomepage"),
  
 
    
]