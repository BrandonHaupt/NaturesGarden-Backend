from django.db import models

# Create your models here.
class NaturesGarden(models.Model):
    url = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    edible = models.CharField(max_length=1000)
    origin = models.CharField(max_length=1000)
    benefits = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)