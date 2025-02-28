from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class CustomerPageTest(SimpleTestCase):
    
    def test_url_exist(self):
        response = self.client.get('/api/customer-page')
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('customer-page'))
        self.assertEqual(response.status_code,200)

    def test_template_name(self):
        response = self.client.get(reverse('customer-page'))
        self.assertTemplateUsed(response,'customer.html')