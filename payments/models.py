from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    balance = models.IntegerField(default=0)
    balanceOwner = models.ForeignKey(User, on_delete=models.CASCADE)