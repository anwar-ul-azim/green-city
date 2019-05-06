from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Cycle(models.Model):

    OwnerId = models.ForeignKey(User, on_delete=models.CASCADE)
    CycleName = models.CharField(max_length=255)
    CycleModelName = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    isPicked = models.BooleanField(default=False)
    # isDroped = models.BooleanField(default=False)
    # state = models.BooleanField(default=False)


class Pickcycle(models.Model):
    locationid = models.CharField(max_length=255)
    cycleid = models.CharField(max_length=255)
    Picker = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_date = models.DateTimeField(default=timezone.now)


class Dropcycle(models.Model):
    locationid = models.CharField(max_length=255)
    cycleid = models.CharField(max_length=255)
    droper = models.ForeignKey(User, on_delete=models.CASCADE)
    drop_date = models.DateTimeField(default=timezone.now)
    

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

    LocationId = models.CharField(max_length=255, choices=LOCATIONID_CHOICES)



