from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from django.views.generic import TemplateView

# Create your views here.

# API view to list all customers and create a new one
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# API view to retrieve, update, or delete a specific customer by ID
class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# View to render the customer HTML page
class CustomerPageView(TemplateView):
    template_name: str = 'customer.html'
