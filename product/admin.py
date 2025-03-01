from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "part_number", "description", "price", "created_at", "updated_at")  # Displayed columns
    search_fields = ("part_number", "description")  # Search by part number or description
    list_filter = ("created_at", "updated_at")  # Enable filtering
    ordering = ("-created_at",)  # Order by newest first
