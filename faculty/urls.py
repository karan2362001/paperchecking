from django.urls import path
from . import views

urlpatterns = [
    path("",views.FacultyHomePage,name="FacultyHomePage")

]
