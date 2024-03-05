from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:  # metadata describing model
        model = Product
        fields = ['title', 'description', 'price', 'summary', 'featured'] # return model throgh API