from django.urls import path
from .views import ProductView, CustomerView, CustomerDetail

urlpatterns = [
    path('products/', ProductView),
    path('customers/', CustomerView),
    path('customers/details/<int:pk>', CustomerDetail),
]