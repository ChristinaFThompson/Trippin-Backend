from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Restaurant, Activity, Trip, CustomUser, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    trips = serializers.HyperlinkedRelatedField(
       # view_trips='trip-detail',
        many=True,
        read_only=True,
        view_name='users'
    )
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    trips = serializers.HyperlinkedRelatedField(
       # view_trips='trip-detail',
        many=True,
        read_only=True,
        view_name='groups'
    )
    """
    class Meta:
        model = Group
        fields = ('id', 'name')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    """
    location = serializers.HyperlinkedRelatedField(
        #view_location='location-detail',
        many=True,
        read_only=True,
        view_name='restaurants'
    )
    """
    class Meta:
        model = Restaurant
        fields = ('locale', 'radius', 'name')

class TripSerializer(serializers.HyperlinkedModelSerializer):
    """
    activity = serializers.HyperlinkedRelatedField(
        #view_activity='restaurant-detail',
        many=True,
        read_only=True,
        view_name='trips'
    )
    """
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

