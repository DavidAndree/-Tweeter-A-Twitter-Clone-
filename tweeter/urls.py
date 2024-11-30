"""
David Alvarado
CIS 218
11/05/24
"""

from django.urls import path
from .views import (
    TwitListView,
    TwitDetailView,
    TwitCreateView,
    TwitUpdateView,
    TwitDeleteView,
    CommentCreateView,
    PublicProfileView,
    like_twit,
)

app_name = 'tweeter'

urlpatterns = [
    # Twit views
    path('', TwitListView.as_view(), name='twit-list'),  # List all Twits
    path('twit/<int:pk>/', TwitDetailView.as_view(), name='twit-detail'),  # Twit detail
    path('twit/new/', TwitCreateView.as_view(), name='twit-create'),  # Create a new Twit
    path('twit/<int:pk>/edit/', TwitUpdateView.as_view(), name='twit-edit'),  # Edit a Twit
    path('twit/<int:pk>/delete/', TwitDeleteView.as_view(), name='twit-delete'),  # Delete a Twit

    # Comment view
    path('twit/<int:twit_id>/comment/', CommentCreateView.as_view(), name='comment-create'),  # Add a comment to a Twit
    
    #Public profile view
    path("profile/<int:pk>/", PublicProfileView.as_view(), name="public-profile"),

    # AJAX view for liking/undo the liking a Twit
    path('twit/<int:twit_id>/like/', like_twit, name='like-twit'),  # Like/Unlike a Twit
]
