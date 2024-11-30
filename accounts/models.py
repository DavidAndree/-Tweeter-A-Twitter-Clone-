"""
David Alvarado
Cis 218
11/05/24
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User Model"""
    
    age =  models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)