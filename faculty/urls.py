from django.urls import path
from . import views

urlpatterns = [
    path("FacultyHomePage/",views.FacultyHomePage,name="FacultyHomePage"),
    path("",views.login,name="login"),
    path("",views.logout,name="logout"),
]
