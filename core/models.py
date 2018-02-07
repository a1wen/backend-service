from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True




