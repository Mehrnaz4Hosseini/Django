from django.urls import path
from .views import review_list, review_detail, CommentList, CommentDetail, ReportList, ReportDetail

urlpatterns = [
    path('reviews/', review_list),
    path('reviews/details/<int:pk>', review_detail),
    path('comments/', CommentList.as_view()),
    path('comments/details/<int:pk>', CommentDetail.as_view()),
    path('reports/', ReportList.as_view()),
    path('reports/details/<int:id>/', ReportDetail.as_view()),
]