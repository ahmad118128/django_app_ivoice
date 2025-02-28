from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('product/<int:pk>/' , views.ProductRetrieveUpdateDestroyView.as_view(), name="product-detail"),
    path('product-page' , views.ProductPageView.as_view(), name="product-page")
]

