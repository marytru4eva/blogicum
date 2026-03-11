from django.test import TestCase
from django.urls import reverse

class IceCreamTests(TestCase):
    def test_ice_cream_list_status_code(self):
        url = reverse('ice_cream:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_ice_cream_detail_status_code(self):
        # Тест для детальной страницы мороженого с id=0
        url = reverse('ice_cream:detail', args=[0])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
