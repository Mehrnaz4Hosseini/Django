from django.urls import path
from .views import review_list, review_detail, CommentList, CommentDetail

urlpatterns = [
    path('reviews/', review_list),
    path('reviews/details/<int:pk>', review_detail),
    path('comments/', CommentList.as_view()),
    path('comments/details/<int:pk>', CommentDetail.as_view()),
]