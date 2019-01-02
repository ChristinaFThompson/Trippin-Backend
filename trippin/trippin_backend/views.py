from django.shortcuts import render
# View is replaced w/API, will use react to issue commands 
# Creating API views, can list data from model

from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from trippin_backend.serializers import UserSerializer
from trippin_backend.serializers import RestaurantSerializer
from trippin_backend.serializers import TripSerializer
from trippin_backend.serializers import ActivitySerializer
from trippin_backend.serializers import GroupSerializer



from .models import Activity, Restaurant, Trip


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('-date_joined')
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

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ActivityList(generics.ListCreateAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer

# class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer

# class RestaurantList(generics.ListCreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class TripList(generics.ListCreateAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer

# class TripDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Trip.objects.all()
#     serializer_class = TripSerializer