from django.db import models
from customer.models import Customer
from product.models import Product



# Choices array
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

 
##### ERD #####
# Table Invoice {
#   id integer [primary key]
#   invoice_number varchar [unique] 
#   customer_id integer [not null]
#   currency_unit varchar
#   payment_method varchar
#   discount_type varchar
#   reference varchar
#   total_amount numeric
#   total_payment numeric
#   vat numeric 
#   discount numeric
#   payment_status varchar
#   issue_date timestamp
#   due_date timestamp
#   created_at timestamp
#   updated_at timestamp
# }
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=255, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')  # هر فاکتور مربوط به یک مشتری است
    currency_unit = models.CharField(max_length=10, blank=True, null=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, blank=True, null=True)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPES, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUSES, blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.invoice_number}"

# Table InvoiceItem {
#   id integer [primary key]
#   invoice_id integer [not null]
#   product_id integer [not null]
#   quantity integer
#   unit_count integer
#   amount_text varchar
#   amount_numeric numeric 
#   vat_percent numeric
#   discount_percent numeric
#   created_at timestamp
#   updated_at timestamp
# }
class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_items')
    quantity = models.IntegerField(blank=True, null=True)
    unit_count = models.IntegerField(blank=True, null=True)
    amount_text = models.CharField(max_length=255, blank=True, null=True)
    amount_numeric = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"InvoiceItem {self.id} (Invoice {self.invoice.invoice_number}, Product {self.product.part_number})"