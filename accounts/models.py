from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User Model"""
    
    age =  models.PositiveIntegerField(null=True, blank=True)