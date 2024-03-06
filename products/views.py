from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer

# Create your API views here.

@csrf_exempt
def ProductView(request):

# get all the products
# serialize them
# return JSON
    
    if request.method == 'GET':    # list all data
        products = Product.objects.all()  # query set
        serializers = ProductSerializer (products, many=True) # make an instance
                                                              # many = True -> serialize all the query set
        return JsonResponse(serializers.data, safe= False)  # safe= False -> return sth like List instead of dictionary
    
    elif request.method == 'POST':  # create data
        data =  JSONParser().parse(request)  # parse -> JSON to python
        serializers = ProductSerializer(data= data)
        if serializers.is_valid():  # manage the error
            serializers.save()
            return JsonResponse(serializers.data, status= 201) # status=201 -> one new resource being created
        return JsonResponse(serializers.errors, status= 400)   # status=400 -> server could not understand
                                                               # the request due to invalid syntax.
    
@csrf_exempt
def CustomerView(request):
    # List all customers, or create a new customer.
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status= 400)

@csrf_exempt
def CustomerDetail(request, pk): # primary key
    # Retrieve, update or delete a custome.
    try:
        customer = Customer.objects.get(pk=pk) #instance
    except Customer.DoesNotExist:
        return HttpResponse(status= 404) # Not found
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer) # we use the instance so -> No many=True
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data= data) # fetch customer and data

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status= 400)
    
    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status= 204)


