from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    LocationName = models.CharField(max_length=255)

    LOCATIONID_CHOICES = (
        ("001", 'L1'),
        ("002", 'L2'),
        ("003", 'L3'),
        ("004", 'L4'),
        ("005", 'L5'),
        ("006", 'L6'),
        ("007", 'L7'),
        ("008", 'L8'),
    )

    LocationId = models.CharField(max_length=255, choices = LOCATIONID_CHOICES)
