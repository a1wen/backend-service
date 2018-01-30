from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import serializers, viewsets, routers
from backendsApp.app import views




router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]