"""
David Alvarado
CIS 218
11/05/24
"""

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Twit, Comment, TwitUserLike, CustomUser

# Twit Views
class TwitListView(ListView):
    """Displays all Twits in reverse chronological order."""
    model = Twit
    template_name = "home.html"
    context_object_name = "twits"
    ordering = ["-created"]  # Most recent first


class TwitDetailView(LoginRequiredMixin, DetailView):
    """Displays details of a single Twit."""
    model = Twit
    template_name = "twit_detail.html"
    context_object_name = "twit"


class TwitCreateView(LoginRequiredMixin, CreateView):
    """Allows authenticated users to create a new Twit."""
    model = Twit
    template_name = "twit_create.html"
    fields = ["body", "image_url"]
    success_url = reverse_lazy("tweeter:twit-list") 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     """Allows the author to update their Twit."""
#     model = Twit
#     template_name = "twit_edit.html"
#     fields = ["body", "image_url"]

#     def test_func(self):
#         return self.get_object().author == self.request.user

class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows the author to update their Twit."""
    model = Twit
    fields = ["body", "image_url"]
    template_name = "twit_edit.html"
    success_url = reverse_lazy("tweeter:twit-list")  # Redirects to the feed

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user


class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Allows the author to delete their Twit."""
    model = Twit
    template_name = "twit_confirm_delete.html"
    success_url = reverse_lazy("tweeter:twit-list")

    def test_func(self):
        return self.get_object().author == self.request.user

# Comment Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    """Allows authenticated users to add comments to a Twit."""
    model = Comment
    template_name = "comment_form.html"
    fields = ["body"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["twit"] = get_object_or_404(Twit, id=self.kwargs["twit_id"])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.twit = get_object_or_404(Twit, id=self.kwargs["twit_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path 

    
class PublicProfileView(DetailView):
    """Displays the public profile of a user."""
    model = CustomUser
    template_name = "public_profile.html"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        # Get the user whose profile is being viewed
        context = super().get_context_data(**kwargs)
        context["twits"] = Twit.objects.filter(author=self.get_object()).order_by("-created")
        context["twits_count"] = context["twits"].count()
        return context
    
# AJAX Views
def like_twit(request, twit_id):
    """Allows users to like/unlike a Twit via AJAX."""
    if request.method == "POST" and request.user.is_authenticated:
        twit = get_object_or_404(Twit, id=twit_id)
        like, created = TwitUserLike.objects.get_or_create(twit=twit, user=request.user)
        if not created:
            like.delete()
            return JsonResponse({"liked": False, "likes_count": twit.likes.count()})
        return JsonResponse({"liked": True, "likes_count": twit.likes.count()})
    return JsonResponse({"error": "Invalid request."}, status=400)
