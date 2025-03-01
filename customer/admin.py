from django.contrib import admin
from .models import Customer

# Customizing the admin panel for the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'mobile', 'fax', 'created_at', 'updated_at')  # Display these fields in the admin list view
    list_filter = ('created_at', 'updated_at')  # Add filters for creation and update dates
    search_fields = ('name', 'phone', 'mobile')  # Enable searching by name, phone, and mobile
    ordering = ('-created_at',)  # Order by most recently created customers first
