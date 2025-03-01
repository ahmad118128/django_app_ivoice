from django.urls import path
from .views import InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView, InvoicePageView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name="invoice-detail"),
    path('invoice-page/', InvoicePageView.as_view(), name="invoice-page"),  # Added trailing slash
]
