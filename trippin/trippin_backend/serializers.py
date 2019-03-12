from django.contrib.auth.models import Group
from .models import Restaurant, Activity, Trip, Location
from rest_framework import serializers
import datetime



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','address','phone', 'name', 'date')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'restaurant_id', 'trip_id', 'username_id', 'date')

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('id','date','username_id', 'latitude', 'longitude')

class LocationSerializer(serializers.ModelSerializer):
         
    class Meta:
        model = Location
        fields = ('longitude', 'latitude')