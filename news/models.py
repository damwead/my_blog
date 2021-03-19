from django.db import models
from django.utils import timezone


# Create your models here.


class Event(models.Model):
    title       = models.CharField(max_length=60)
    # poster      = models.ImageField(upload_to='uploads')
    description = models.TextField(max_length=10000, blank=True, null=True)
    date        = models.DateField(null=True, blank=True)
    place       = models.CharField(max_length=20, null=True, blank=True)
