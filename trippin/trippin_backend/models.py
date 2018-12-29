from django.db import models

# Create your models here.
class Activity(models.Model):
    restaurant = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)

def __str__(self):
    return self.restaurant


class restaurant(models.Model):
    location = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)

def __str__(self):
    return self.location


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.email


    