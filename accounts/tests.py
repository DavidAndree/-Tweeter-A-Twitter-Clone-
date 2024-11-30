"""
David Alvarado
Cis 218
11/05/24
"""

from django.contrib.auth import get_user_model 
from django.test import TestCase 
from django.urls import reverse


class SignUpTestPage(TestCase):
    """Sign Up Page Test"""
    
    def test_url_exist_at_correct_location_signupview(self):
        """Test URL exist at correct location signup view"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        
    def test_signup_view_name(self):
        """Test Sign Up View Name"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
             
    def test_signup_form(self):
        """Test Sign Up Form"""
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testexample@gmail.com",
                "password1": "password",
                "password2": "password",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testexample@gmail.com")