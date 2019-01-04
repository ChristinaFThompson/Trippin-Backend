from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Restaurant, Activity, Trip, CustomUser, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Group
        fields = ('id', 'name')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = ('locale', 'radius', 'name')

class TripSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Trip
        fields = ('username', 'date', 'memories')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Activity
        fields = ('username', 'restaurant', 'trip')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # list 10 restaurants via the Yelp API
    class Meta:
        model = Location
        fields = ('longitude', 'latitude')

