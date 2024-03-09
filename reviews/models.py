from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# any change here -> python manage.py makemigrations
#                    python manage.py migrate

class Review(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        string_user_id = str(self.user_id)
        return string_user_id + ' -> ' + self.title
    

class Comment(models.Model):
    user_id = models.IntegerField()
    review_id = models.IntegerField()
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    review = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
