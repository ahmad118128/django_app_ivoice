from django.urls import path
from . import views

urlpatterns = [
    # List all customers and create a new one
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list-create'),

    # Retrieve, update, or delete a specific customer by ID
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroyView.as_view(), name="customer-detail"),

    # Customer page view (e.g., for rendering an HTML page)
    path('customer-page/', views.CustomerPageView.as_view(), name="customer-page"),
]
