"""
David Alvarado
Cis 218
11/05/24
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """ Custom User Creation Form """
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
        
class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form """
    
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "age", "first_name", "last_name", "date_of_birth"] 