from django.db import models
from django.contrib.auth.models import User

from core.models import AbstractModel


class Organizator(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizathion = models.CharField(max_length=100)

