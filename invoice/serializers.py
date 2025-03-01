from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    formatted_issue_date = serializers.DateTimeField(source='issue_date', format='%Y-%m-%d', read_only=True)
    formatted_due_date = serializers.DateTimeField(source='due_date', format='%Y-%m-%d', read_only=True)
    total_amount_display = serializers.SerializerMethodField()
    total_payment_display = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_number', 'customer', 'customer_name', 'currency_unit',
            'payment_method', 'discount_type', 'reference', 'total_amount',
            'total_payment', 'vat', 'discount', 'payment_status',
            'formatted_issue_date', 'formatted_due_date', 'created_at', 'updated_at',
            'total_amount_display', 'total_payment_display'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_total_amount_display(self, obj):
        return f"{obj.total_amount} {obj.currency_unit}" if obj.total_amount else None

    def get_total_payment_display(self, obj):
        return f"{obj.total_payment} {obj.currency_unit}" if obj.total_payment else None
