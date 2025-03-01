from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# View to list all posts and create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset: generics.QuerySet[Post] = Post.objects.all()  # Fetch all posts
    serializer_class: type[PostSerializer] = PostSerializer  # Define serializer class

# View to retrieve, update, and delete a specific post by ID
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset: generics.QuerySet[Post] = Post.objects.all()  # Fetch all posts
    serializer_class: type[PostSerializer] = PostSerializer  # Define serializer class
