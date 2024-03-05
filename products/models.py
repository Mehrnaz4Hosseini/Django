from django.db import models

# any change here -> python manage.py makemigrations
#                    python manage.py migrate
            

class Product(models.Model):          # parent class -> the class inherits all the attributes from models.Model
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True) # blank = True -> we can leave the description empty on site
                                                          # null = True  -> description in database can be null
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    summary     = models.TextField(blank=False, null=False) # summary is required
    featured    = models.BooleanField(null=True) # null=True / default=value 
    

class Customer(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName  = models.CharField(max_length=30)
    age       = models.IntegerField()

    def __str__ (self):
        return self.FirstName + ' ' + self.LastName # show this instead of just the title in the list of Customer on site
