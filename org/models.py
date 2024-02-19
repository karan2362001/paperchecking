from django.db import models
from api.models import CustomUser
# Create your models here.

class FacultyDetails(models.Model):
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)