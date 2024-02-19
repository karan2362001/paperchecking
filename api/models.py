from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)