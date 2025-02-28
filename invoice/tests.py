from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class InvoicePageTest(SimpleTestCase):
    
    def test_url_exist(self):
        response = self.client.get('/api/invoice-page')
        self.assertEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('invoice-page'))
        self.assertEqual(response.status_code,200)

    def test_template_name(self):
        response = self.client.get(reverse('invoice-page'))
        self.assertTemplateUsed(response,'invoice.html')