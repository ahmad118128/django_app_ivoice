from django.test import SimpleTestCase
from django.urls import reverse

class InvoicePageTest(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        """Test if the invoice page is accessible via the correct URL."""
        url = reverse('invoice-page')  # Always use reverse()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test if the invoice page is accessible by its name in urls.py."""
        response = self.client.get(reverse('invoice-page'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """Ensure the correct template is used to render the page."""
        response = self.client.get(reverse('invoice-page'))
        self.assertTemplateUsed(response, 'invoice.html')

    def test_page_contains_expected_content(self):
        """Verify that the invoice page contains expected text."""
        response = self.client.get(reverse('invoice-page'))
        self.assertContains(response, "<h1>Invoice Page</h1>")  # Modify based on actual HTML
