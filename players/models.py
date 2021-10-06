from django.db import models

# Create your models here.
class Players(models.Model):
    playername = models.CharField(max_length=255)
    playeremail = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    games = models.CharField(max_length=255)
    score = models.FloatField()
