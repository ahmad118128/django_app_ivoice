from rest_framework import serializers
from .models import Post

# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Post] = Post  # Define the model for serialization
        fields: str = '__all__'  # Serialize all fields of the model
