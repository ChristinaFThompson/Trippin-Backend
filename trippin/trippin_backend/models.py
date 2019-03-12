from django.db import models
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from users.models import CustomUser

# Create your models here.
class Restaurant(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True, editable=True)
    phone = models.CharField(max_length=30, null=True, blank=True, editable=True)
    name =  models.TextField(max_length=100, null=True, blank=True, editable=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)


class Trip(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    longitude = models.FloatField(null=True, blank=True, default=38.994972)
    latitude =  models.FloatField(null=True, blank=True, default=-77.024762)

class Activity(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)
    longitude = models.FloatField(null=True, blank=True, default=38.994972)
    latitude =  models.FloatField(null=True, blank=True, default=-77.024762)

class Location(models.Model):
    longitude = models.FloatField(null=True, blank=True, default=38.994972)
    latitude =  models.FloatField(null=True, blank=True, default=-77.024762)