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
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
