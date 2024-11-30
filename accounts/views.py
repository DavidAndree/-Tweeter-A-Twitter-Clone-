"""
David Alvarado
Cis 218
11/05/24
"""

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .models import CustomUser  
from .forms import ProfileEditForm


class  SignUpView(CreateView):
    """Sign Up View"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser 
    form_class = ProfileEditForm
    template_name = "profile_edit.html"  
    success_url = reverse_lazy("home")  

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:profile-edit")