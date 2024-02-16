from django.urls import path
from . import views

urlpatterns = [
    path("/adminHomepage/",views.adminHomepage,name="adminHomepage"),
    path("",views.login,name="login"),
    path("/logout/",views.logout, name='logout'),
 
    
]