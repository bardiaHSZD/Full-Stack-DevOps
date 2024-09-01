from django.db import models

# Create your models here.
from unicodedata import name

class Menu(models.Model):
    name = models.CharField(max_length= 100)
    cuisine = models.CharField(max_length= 100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name + ":" +  self.cuisine
    

class Logger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    time_log = models.TimeField()


class Reservations(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name




    