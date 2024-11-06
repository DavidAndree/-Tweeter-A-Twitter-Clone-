"""
David Alvarado
Cis 218
11/05/24
"""

from accounts.models import CustomUser
from django.db import models


class Twit(models.Model):
    """ Twit Model """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="twits")
    body = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username}: {self.body[:20]}"

class Comment(models.Model):
    """ Comment Model """
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} on Twit {self.twit.id}: {self.body[:20]}"

class TwitUserLike(models.Model):
    """ Twit Like Model (for storing likes) """
    
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_twits")

    class Meta:
        unique_together = ('twit', 'user')

    def __str__(self):
        return f"{self.user.username} likes Twit {self.twit.id}"