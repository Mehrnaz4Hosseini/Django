from django.urls import path
from .views import review_list, review_detail

urlpatterns = [
    path('reviews/', review_list),
    path('reviews/details/<int:pk>', review_detail),
]