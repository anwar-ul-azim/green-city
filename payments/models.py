from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    balanceOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    earned = models.IntegerField(default=0)
    due = models.IntegerField(default=0)

class Transition(models.Model):
    sender = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='receiver', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

class CashInOrOut(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    cash_in = models.IntegerField(default=0)
    cash_out = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
