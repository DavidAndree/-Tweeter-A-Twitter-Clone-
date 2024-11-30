from django.test import TestCase, Client
from django.urls import reverse
from .models import Twit, Comment, TwitUserLike
from accounts.models import CustomUser


class ExtendedTweeterAppTests(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username="testuser", email="test@test.com", password="password123"
        )
        self.other_user = CustomUser.objects.create_user(
            username="otheruser", email="other@test.com", password="password456"
        )
        self.twit = Twit.objects.create(author=self.user, body="Test Twit")
        self.comment = Comment.objects.create(
            author=self.other_user, twit=self.twit, body="Test Comment"
        )

    def test_access_without_login(self):
        """Ensure views redirect to login for unauthenticated users."""
        response = self.client.get(reverse("tweeter:twit-list"))
        self.assertEqual(response.status_code, 302)  
        response = self.client.get(reverse("tweeter:twit-create"))
        self.assertEqual(response.status_code, 302)  

    def test_twit_list_view_no_twit(self):
        """Test the Twit list view when no Twits exist."""
        self.twit.delete()
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("tweeter:twit-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Twits yet. Start by creating a new one!")

    def test_twit_creation_invalid_data(self):
        """Ensure Twit creation fails with invalid data."""
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("tweeter:twit-create"), {"body": ""})
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(Twit.objects.filter(body="").exists())

    def test_comment_creation_invalid_data(self):
        """Ensure comment creation fails with invalid data."""
        self.client.login(username="otheruser", password="password456")
        response = self.client.post(
            reverse("tweeter:comment-create", args=[self.twit.pk]), {"body": ""}
        )
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(Comment.objects.filter(body="").exists())

    def test_like_twit_multiple_times(self):
        """Ensure liking a Twit multiple times doesn't create duplicate likes."""
        self.client.login(username="testuser", password="password123")
        self.client.post(reverse("tweeter:like-twit", args=[self.twit.pk]))
        self.client.post(reverse("tweeter:like-twit", args=[self.twit.pk]))
        self.assertEqual(TwitUserLike.objects.filter(twit=self.twit, user=self.user).count(), 1)

    def test_twit_edit_other_user(self):
        """Ensure a user cannot edit another user's Twit."""
        self.client.login(username="otheruser", password="password456")
        response = self.client.post(
            reverse("tweeter:twit-edit", args=[self.twit.pk]), {"body": "Hacked Twit"}
        )
        self.assertEqual(response.status_code, 403) 
        self.twit.refresh_from_db()
        self.assertNotEqual(self.twit.body, "Hacked Twit")

    def test_twit_delete_other_user(self):
        """Ensure a user cannot delete another user's Twit."""
        self.client.login(username="otheruser", password="password456")
        response = self.client.post(reverse("tweeter:twit-delete", args=[self.twit.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Twit.objects.filter(pk=self.twit.pk).exists())

    def test_twit_like_count(self):
        """Ensure the like count updates correctly."""
        self.client.login(username="testuser", password="password123")
        self.client.post(reverse("tweeter:like-twit", args=[self.twit.pk]))
        self.assertEqual(self.twit.likes.count(), 1)
        self.client.post(reverse("tweeter:like-twit", args=[self.twit.pk]))  
        self.assertEqual(self.twit.likes.count(), 0)

    def test_twit_list_view_shows_comments(self):
        """Ensure the Twit detail view displays comments."""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("tweeter:twit-list", args=[self.twit.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Comment")

    def test_twit_delete_redirect(self):
        """Ensure deleting a Twit redirects correctly."""
        self.client.login(username="testuser", password="password123")
        response = self.client.post(reverse("tweeter:twit-delete", args=[self.twit.pk]))
        self.assertRedirects(response, reverse("tweeter:twit-list"))

    def test_profile_page(self):
        """Ensure the profile page displays user details and Twits."""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("tweeter:public-profile", args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")
        self.assertContains(response, "Test Twit")
