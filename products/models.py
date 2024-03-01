from django.db import models

# Create your models here.

class Product(models.Model):          # parent class -> the class inherits all the attributes from models.Model
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default = 'Whatever you want.')