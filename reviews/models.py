from django.db import models

# any change here -> python manage.py makemigrations
#                    python manage.py migrate

class Review(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)