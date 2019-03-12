from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from . import views 
from django.urls import include, path

"""
urlpatterns = [
url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
url(r'^api/v1/locate', views.ListRestaurants.as_view(), name='rest-list'),
]
urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),

    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^locate/', views.ListRestaurants.as_view(), name='rest-list'),
    path('trip/', views.CreateTrip.as_view()),
]
"""
urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^locate/', views.ListRestaurants.as_view(), name='rest-list'),
    path('trip/', views.CreateTrip.as_view()),
    path('activity/', views.CreateActivity.as_view()),
    path('activity/', views.CreateActivity.as_view()),
    path('restaurant/', views.CreateRestaurant.as_view()),
]




