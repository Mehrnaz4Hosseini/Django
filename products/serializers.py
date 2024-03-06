# serialize -> turning data into JSON
from rest_framework import serializers
from .models import Product, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:  # metadata describing model
        model = Product
        fields = ['title', 'description', 'price', 'summary', 'featured'] # return model throgh API


class CustomerSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=30)
    LastName  = serializers.CharField(max_length=30)
    age       = serializers.IntegerField()

    def create(self, validated_data):
        return Customer.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.FirstName = validated_data.get('FirstName', validated_data.FirstName)
        instance.LastName = validated_data.get('LastName', validated_data.LastName)
        instance.age = validated_data.get('age', validated_data.age)