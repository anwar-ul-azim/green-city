from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


def upload_image_to(instance, filename):
    return 'cycle/cycle_{0}/{1}'.format(instance.pk, filename)

class Cycle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    image = models.ImageField(upload_to=upload_image_to)
    is_picked = models.BooleanField(default=False)
    rent = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    picked_times = models.IntegerField(default=0)
    

class Pickcycle(models.Model):
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    picked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_date = models.DateTimeField(auto_now = True)


class Dropcycle(models.Model):
    cycle_id = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    drop_by = models.ForeignKey(User, on_delete=models.CASCADE)
    drop_date = models.DateTimeField(auto_now = True)
    

class Location(models.Model):
    area = models.CharField(max_length=30)
    near_by = models.CharField(max_length=30)
    near_by_t = models.CharField(max_length=30)
    gps_lat = models.CharField(max_length=30)
    gps_lon = models.CharField(max_length=30)
    cycle_id = models.OneToOneField(Cycle, on_delete=models.CASCADE)


