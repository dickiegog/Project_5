from django.test import TestCase
from django.urls import reverse
from .models import Newsletter

class NewsletterSignupTest(TestCase):
    def test_newsletter_signup(self):
        response = self.client.post(reverse('newsletter_signup'), {
            'email': 'test@example.com'
        })
        # Check that the user is redirected (to home)
        self.assertEqual(response.status_code, 302)
        # Check that the email was saved
        self.assertTrue(Newsletter.objects.filter(email='test@example.com').exists())
