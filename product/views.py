from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductPageView(View):
#     def get(self , request):
#         return render(request ,'Product.html')


class ProductPageView(TemplateView):
    template_name = 'product.html'

