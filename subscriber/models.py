from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from core.models import AbstractModel
from project.models import Project


class Subscriber(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Project, on_delete=models.CASCADE)
