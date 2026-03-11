

from django.test import TestCase
from django.urls import reverse

class AboutTests(TestCase):
    def test_about_page_status_code(self):
        url = reverse('about:description')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
