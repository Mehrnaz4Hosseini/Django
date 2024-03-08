from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields= ['user_id', 'product_id', 'title', 'body', 'rating', 'date_posted']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields= ['user_id', 'review_id', 'body', 'date_posted']