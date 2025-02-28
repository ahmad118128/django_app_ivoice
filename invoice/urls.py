from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoice/<int:pk>/' , views.InvoiceRetrieveUpdateDestroyView.as_view(), name="invoice-detail"),
    path('invoice-page' , views.InvoicePageView.as_view(), name="invoice-page")
]

