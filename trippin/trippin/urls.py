from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from trippin_backend import views
from django.contrib import admin
from django.urls import path
from django.urls import include, path


router = routers.DefaultRouter()
#router.register(r'users', UserListView)
router.register(r'groups', views.GroupViewSet)
"""
router.register(r'Trips', views.TripViewSet)
router.register(r'Restaurants', views.RestaurantViewSet)
router.register(r'Activities', views.ActivityViewSet)
router.register(r'Locations', views.LocationViewSet)
"""
"""
urlpatterns = [
    url(r'^', include('trippin_backend.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
]
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('trippin_backend.urls')),
    url(r'^', include(router.urls)),
]
