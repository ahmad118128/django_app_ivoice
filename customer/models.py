from django.db import models

# Create your models here.
# Table Customer {
#   id integer [primary key]
#   name varchar
#   phone varchar
#   mobile varchar
#   fax varchar
#   created_at timestamp
#   updated_at timestamp
# }

# Model representing a customer
class Customer(models.Model):
    id: int = models.AutoField(primary_key=True)  # Unique ID for each customer
    name: str = models.CharField(max_length=255)  # Customer name (required)
    phone: str | None = models.CharField(max_length=20, blank=True, null=True)  # Landline phone number (optional)
    mobile: str | None = models.CharField(max_length=20, blank=True, null=True)  # Mobile phone number (optional)
    fax: str | None = models.CharField(max_length=20, blank=True, null=True)  # Fax number (optional)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)  # Timestamp when the record is created
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)  # Timestamp when the record is last updated

    def __str__(self) -> str:
        """Returns a string representation of the customer (their name)."""
        return self.name
