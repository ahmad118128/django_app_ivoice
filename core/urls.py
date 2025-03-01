from django.urls import path
from . import views

# Define URL patterns for Post views
urlpatterns: list[path] = [
    # Endpoint for listing and creating posts
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),

    # Endpoint for retrieving, updating, and deleting a single post by primary key (pk)
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
]
