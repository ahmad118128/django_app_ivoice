from django.test import TestCase
from django.urls import reverse

class ProductPageTest(TestCase):
    
    def test_url_exists(self):
        response = self.client.get('/api/product-page/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('product-page'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_used(self):
        response = self.client.get(reverse('product-page'))
        self.assertTemplateUsed(response, 'product.html')
