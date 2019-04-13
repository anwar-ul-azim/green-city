from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Dropcycle(models.Model):
    locationid = models.CharField(max_length=255)
    cycleid = models.CharField(max_length=255)
    droper = models.ForeignKey(User, 
    on_delete=models.CASCADE)
    drop_date = models.DateTimeField(default=timezone.now)

    