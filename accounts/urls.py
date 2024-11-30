"""
David Alvarado
Cis 218
11/05/24
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileEditView

urlpatterns=[
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]