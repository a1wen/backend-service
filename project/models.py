from django.db import models
from django.utils import timezone

from core.models import  AbstractModel

# Create your models here.
LEVEL_CHOICES = (
    ('low', "Низикий"),
    ('medium', "Средний"),
    ('high', "Высокий"),
    ('veryhigh',  "Очень высокий",)
)

class Project(AbstractModel):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    levelOfTraining = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="medium")


    def __str__(self):
        return self.name