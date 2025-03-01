from django.db import models
from customer.models import Customer
from product.models import Product

# Choice options for different fields
PAYMENT_METHODS = [
    ('cash', 'Cash'),
    ('credit_card', 'Credit Card'),
    ('bank_transfer', 'Bank Transfer'),
]

DISCOUNT_TYPES = [
    ('percentage', 'Percentage'),
    ('fixed', 'Fixed Amount'),
]

PAYMENT_STATUSES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('overdue', 'Overdue'),
    ('cancelled', 'Cancelled'),
]

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=255, unique=True, verbose_name="Invoice Number")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices', verbose_name="Customer")
    currency_unit = models.CharField(max_length=10, blank=True, null=True, verbose_name="Currency Unit")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, blank=True, null=True, verbose_name="Payment Method")
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, blank=True, null=True, verbose_name="Discount Type")
    reference = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reference")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Total Amount")
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Total Payment")
    vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="VAT")
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Discount")
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, blank=True, null=True, verbose_name="Payment Status")
    issue_date = models.DateTimeField(blank=True, null=True, verbose_name="Issue Date")
    due_date = models.DateTimeField(blank=True, null=True, verbose_name="Due Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self) -> str:
        return f"Invoice {self.invoice_number} - {self.customer.name}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items', verbose_name="Invoice")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_items', verbose_name="Product")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    unit_count = models.PositiveIntegerField(default=1, verbose_name="Unit Count")
    amount_text = models.CharField(max_length=255, blank=True, null=True, verbose_name="Amount (Text)")
    amount_numeric = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Amount (Numeric)")
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="VAT (%)")
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Discount (%)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"

    def __str__(self) -> str:
        return f"Invoice {self.invoice.invoice_number} - Product {self.product.part_number}"
