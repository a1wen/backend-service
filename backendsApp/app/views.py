from django.shortcuts import render
from rest_framework import viewsets

from backendsApp.app.serializers import ProjectSerializer
from project.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

