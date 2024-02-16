from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("admin/",views.adminUser.as_view(),name="adminUser"),
      path("admin/<int:pk>/",views.adminUser.as_view(),name="adminUser"),
     
]