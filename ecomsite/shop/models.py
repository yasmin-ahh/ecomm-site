from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    catgory = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Order(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    items= models.CharField(max_length=2000, default='some_value')
    total = models.CharField(max_length=1000, default='0')
