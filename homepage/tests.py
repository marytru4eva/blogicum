from django.test import TestCase
from django.urls import reverse

class HomepageTests(TestCase):
    def test_homepage_status_code(self):
        url = reverse('homepage:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
