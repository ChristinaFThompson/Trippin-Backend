from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# will use for auth later. 
class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Restaurant(models.Model):
    locale = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)
    name =  models.TextField(max_length=100, null=True, blank=True, editable=True)


class Trip(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    memories = models.TextField(max_length=200, null=True, blank=True)


class Activity(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)

class Location(models.Model):
    longitude = models.FloatField(null=True, blank=True, default=38.994972)
    latitude = models.FloatField(null=True, blank=True, default=-77.024762)

