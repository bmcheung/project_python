from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length = 50)
    breed = models.CharField(max_length = 50)
    location_lost = models.CharField(max_length = 255)
    date_lost = models.DateField()
    status = models.CharField(max_length = 20)
    notes = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
