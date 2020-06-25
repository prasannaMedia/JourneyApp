from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.CharField(max_length=30)
    rem = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    time = models.TimeField()




class Book(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.CharField(max_length=30)
    busid=models.CharField(max_length=30)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    cost = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()


