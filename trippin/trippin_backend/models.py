from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Restaurant(models.Model):
    locale = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)
    name =  models.TextField(max_length=100, null=True, blank=True, editable=True)


class Trip(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    date = models.DateTimeField(max_length=30)
    memories = models.TextField(max_length=200, null=True, blank=True)


class Activity(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)