from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="profileuser", password="testpass")
        self.profile, created = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={
                "address": "123 Main St",
                "city": "Testville",
                "postal_code": "12345",
                "country": "IE",
                "phone_number": "1234567890"
            }
        )

    def test_profile_str(self):
        self.assertIn("profileuser", str(self.profile))
