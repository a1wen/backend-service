from django.db import models
from django.utils import timezone
from django.conf import settings

from core.models import  AbstractModel

# Create your models here.
from organizators.models import Organizator

LEVEL_CHOICES = (
    ('low', "Низикий"),
    ('medium', "Средний"),
    ('high', "Высокий"),
    ('veryhigh',  "Очень высокий",)
)

class Project(AbstractModel):
    # id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    levelOfTraining = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="medium")
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

