from django.db import models

# Create your models here.

# Table Product {
#   id integer [primary key]
#   description varchar
#   part_number varchar [unique] 
#   price numeric
#   created_at timestamp
#   updated_at timestamp
# }
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)  # شرح کالا
    part_number = models.CharField(max_length=100, unique=True)  # Part.No
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.part_number} - {self.description}"
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)  # شرح کالا
    part_number = models.CharField(max_length=100, unique=True)  # Part.No
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.part_number} - {self.description}"
   