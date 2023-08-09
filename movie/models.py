from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url= models.URLField(blank=True)
    

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    opening_time = models.TimeField(default="07:00:00")
    closing_time = models.TimeField(default="18:00:00")

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100)
    dish_description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)