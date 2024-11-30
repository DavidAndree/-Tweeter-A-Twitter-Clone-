"""
David Alvarado
Cis 218
11/05/24
"""

from django.contrib import admin
from .models import Twit, Comment, TwitUserLike

@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
    list_display = ("body", "author", "created", "updated")
    search_fields = ("body", "author__username")
    list_filter = ("created", "updated")
    ordering = ("-created",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("body", "author", "twit", "created", "updated")
    search_fields = ("body", "author__username", "twit__body")
    list_filter = ("created", "updated")

@admin.register(TwitUserLike)
class TwitUserLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "twit")
    search_fields = ("user__username", "twit__body")
    list_filter = ("twit__created",)