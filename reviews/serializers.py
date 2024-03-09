from rest_framework import serializers
from .models import Review, Comment, Report

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields= ['user_id', 'product_id', 'title', 'body', 'rating', 'date_posted']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields= ['user_id', 'review_id', 'body', 'date_posted']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model= Report
        fields= ['review', 'user', 'reason', 'created_at']