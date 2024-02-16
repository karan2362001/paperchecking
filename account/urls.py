from django.urls import path
from . import views

urlpatterns = [

    path("",views.login,name="login"),
    path("logout/",views.logout, name='logout'),
    path("facultyHomepage/",views.facultyHomepage,name="facultyHomepage"),
    path("adminHomepage/",views.adminHomepage,name="adminHomepage"),
     
]