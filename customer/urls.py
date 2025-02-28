from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customer/<int:pk>/' , views.CustomerRetrieveUpdateDestroyView.as_view(), name="customer-detail"),
    path('customer-page' , views.CustomerPageView.as_view(), name="customer-page")
]

