from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Restaurant, Activity, Trip, Location
from users.models import CustomUser
from rest_framework import viewsets
from trippin_backend.serializers import GroupSerializer, RestaurantSerializer, ActivitySerializer, TripSerializer, LocationSerializer
from users.serializers import UserSerializer

import requests
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token

from rest_framework import generics
from django.http import HttpResponse, JsonResponse

API_KEY = "_zgpe0E9B_49nkcuC8d6Um0230IDE3Okwu0X01grMO_yYl4ZiElcTVpCoUbdd0cDQPu67IATiZ9kCISQWdSb5uvg0fc5e0nuhRhptQknSilDrzIXqRXr7Rm5eeQsXHYx"  


# API constants, you shouldn't have to change these.

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
DEFAULT_TERM = 'restaurants'
SEARCH_LIMIT = 5
DEFAULT_RADIUS = 10000

# Create your views here.

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RestaurantViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ActivityViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class TripViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows trips to be viewed or edited.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class LocationViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows trips to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ListRestaurants(APIView):
    """ 
    Returns a list of restaurants based on location.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, format='json'):
        
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            url_params = {}
            url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
            headers = {
                'Authorization': 'Bearer %s' % API_KEY,
            }
            url_params = {
                'term': DEFAULT_TERM.replace(' ', '+'),
                'latitude': float(request.data["latitude"]),
                'longitude': float(request.data["longitude"]),
                'limit': SEARCH_LIMIT, 
                'radius': DEFAULT_RADIUS,
                'sort_by': 'distance'
            }
            data = requests.request('GET', url, headers=headers, params=url_params)
            return Response(data.json(), status=status.HTTP_200_OK)
        else:
            pass

class CreateTrip(APIView):
    """ 
    Creates a trip.
    """
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def post(self, request, format='json'):

        trip = Trip(username=request.user, latitude=request.data["latitude"], longitude=request.data["longitude"] )
        trip.save()

        data = TripSerializer(trip)

        return JsonResponse(data.data, safe=False)

    """    
    def get(self, request, format='json'):

        trips = Trip.objects.all().filter(username=request.user)
        print(trips)
        for t in trip:
            act = Activity.objects.all().filter
            (pk)
            ActivitySerializer(actions[0])
            Activity.objects.all().filter(username=request.user)
            food = Restaurant.objects.get(pk=data.data["restaurant_id"])
        
            data = RestaurantSerializer(food)
        return JsonResponse(data.data, safe=False)
    """

class CreateRestaurant(APIView):
    """ 
    Creates a restaurant.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def post(self, request, format='json'):

        restaurant = Restaurant(phone=request.data["phone"], address=request.data["address"], name=request.data["eatery"])
        restaurant.save()

        data = RestaurantSerializer(restaurant)

        return JsonResponse(data.data, safe=False)


class CreateActivity(APIView):
    """ 
    Creates a restaurant.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def post(self, request, format='json'):

        activity = Activity(username=request.user, restaurant=Restaurant.objects.get(pk=request.data["food"]), trip=Trip.objects.get(pk=request.data["vacay"]))
        activity.save()

        data = ActivitySerializer(activity)

        return JsonResponse(data.data, safe=False)


    def get(self, request, format='json'):

        fun = []
        food = []
        display = []
        trip = Trip.objects.all().filter(username=request.user).order_by('-date')
        actions = Activity.objects.all().filter(trip=trip[0]).order_by('date')
        
        for a in actions:
            fun.append(ActivitySerializer(a).data)

        for f in fun:
            food.append(Restaurant.objects.get(pk=f["restaurant_id"]))

        for f in food:
            display.append(RestaurantSerializer(f).data)

        print(display)

        return JsonResponse(display, safe=False)