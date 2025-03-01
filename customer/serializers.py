from rest_framework import serializers
from .models import Customer

# Serializer for the Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model: type[Customer] = Customer  # Define the model to serialize
        fields: str = '__all__'  # Include all model fields in the serializer
