from django.shortcuts import render
# View is replaced w/API, will use react to issue commands 
# Creating API views, can list data from model

from rest_framework import viewsets
from django.contrib.auth.models import Group
from trippin_backend.serializers import UserSerializer
from trippin_backend.serializers import RestaurantSerializer
from trippin_backend.serializers import TripSerializer
from trippin_backend.serializers import ActivitySerializer
from trippin_backend.serializers import GroupSerializer
from trippin_backend.serializers import LocationSerializer
from rest_framework.views import APIView

import requests
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Activity, Restaurant, Trip, CustomUser, Location

API_KEY = "_zgpe0E9B_49nkcuC8d6Um0230IDE3Okwu0X01grMO_yYl4ZiElcTVpCoUbdd0cDQPu67IATiZ9kCISQWdSb5uvg0fc5e0nuhRhptQknSilDrzIXqRXr7Rm5eeQsXHYx" 


# API constants, dont change.
# const used to access yelp API
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/' # Business ID will come after slash.


# Default example.
DEFAULT_TERM = 'restaurants'
DEFAULT_LOCATION = 'Washington, D.C.'
DEFAULT_LAT = 38.994972
DEFAULT_LONG = -77.024762
SEARCH_LIMIT = 5
DEFAULT_RADIUS = 500

# yelp API view function

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
            }
            # sends GET request yelp fusion api, response is stored in data, return data in JSON to frontend
            data = requests.request('GET', url, headers=headers, params=url_params)
            return Response(data.json(), status=status.HTTP_200_OK)
        else:
            print("\nINVALID DATA\n")




class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

