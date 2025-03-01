from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.exceptions import NotFound
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Invoice.DoesNotExist:
            raise NotFound({"error": "Invoice not found"})

class InvoicePageView(TemplateView):
    template_name = 'invoice.html'  # Ensure 'invoice.html' exists in the templates folder
