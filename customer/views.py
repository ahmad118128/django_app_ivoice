from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# class CustomerPageView(View):
#     def get(self , request):
#         return render(request ,'Customer.html')


class CustomerPageView(TemplateView):
    template_name = 'customer.html'

