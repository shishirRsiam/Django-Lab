from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=201, blank=True)
    location = models.CharField(max_length=30, blank=True)
