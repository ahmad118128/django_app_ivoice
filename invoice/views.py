from rest_framework import generics
from .models import Invoice
from .serializers import InvoiceSerializer
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# class InvoicePageView(View):
#     def get(self , request):
#         return render(request ,'invoice.html')


class InvoicePageView(TemplateView):
    template_name = 'invoice.html'

