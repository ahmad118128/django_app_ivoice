from django.test import TestCase
from django.urls import reverse

# Tests for the Customer page
class CustomerPageTest(TestCase):  # Changed from SimpleTestCase to TestCase
    
    def test_url_exists(self) -> None:
        """Test if the customer page URL is accessible directly."""
        response = self.client.get(reverse('customer-page'))  # Use reverse() instead of a hardcoded URL
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self) -> None:
        """Test if the customer page is accessible using the named URL."""
        response = self.client.get(reverse('customer-page'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self) -> None:
        """Test if the correct template is used for the customer page."""
        response = self.client.get(reverse('customer-page'))
        self.assertTemplateUsed(response, 'customer.html')  # Ensure the template exists
