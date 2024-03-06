from django.urls import path
from .views import ProductView, CustomerView

urlpatterns = [
    path('products/', ProductView),
    path('customers/', CustomerView),
]