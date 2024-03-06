from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer

# Create your API views here.


def products_list(request):

# get all the products
# serialize them
# return JSON
    
    if request == 'GET':    # list all data
        products = Product.objects.all()  # query set
        serializers = ProductSerializer (products, many=True) # make an instance
                                                              # many = True -> serialize all the query set
        return JsonResponse(serializers.data, safe= False)  # safe= False -> return sth like List instead of dictionary
    
    elif request == 'POST':  # create data
        data =  JSONParser().parse(request)  # parse -> JSON to python
        serializers = ProductSerializer(data = data)

        if serializers.is_valid():  # manage the error
            serializers.save()
            return JsonResponse(serializers.data, status= 201) # status=201 -> one new resource being created
        return JsonResponse(serializers.errors, status= 400)   # status=400 -> server could not understand
                                                               # the request due to invalid syntax.

