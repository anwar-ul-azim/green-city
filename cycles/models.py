from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Cycle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    isPicked = models.BooleanField(default=False)
    rent = models.IntegerField()
    rating = models.IntegerField()
    picked = models.IntegerField()
    

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
    area = models.CharField(max_length=255)
    nearByF = models.CharField(max_length=255)
    nearByS = models.CharField(max_length=255)
    gpsLat = models.CharField(max_length=255)
    gpsLan = models.CharField(max_length=255)
    cycleid = models.OneToOneField(Cycle, on_delete=models.CASCADE)


