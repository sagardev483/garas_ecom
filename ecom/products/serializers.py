from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "get_absolute_url",
            "name",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "stock",
        )
        
class CategorySerializer(serializers.ModelSerializer):  
    
    
    class Meta:
        model = Category
        fields = (
            "id",
            "get_absolute_url",
            "name",
            "description",
            
        )