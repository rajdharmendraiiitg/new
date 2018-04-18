from django.db import models
from datetime import datetime

class CarData(models.Model):
    carname = models.CharField(max_length=30)
    quantity = models.IntegerField()
    cartype = models.CharField(max_length=10)
    carimage = models.FileField()

class RentData(models.Model):
    username = models.CharField(max_length=20)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    start = models.DateTimeField(default=datetime.now, blank=True)
    end = models.DateTimeField(default=datetime.now, blank=True)
    carname = models.CharField(max_length=30)
    ccno = models.CharField(max_length=20)
    cost = models.IntegerField()
