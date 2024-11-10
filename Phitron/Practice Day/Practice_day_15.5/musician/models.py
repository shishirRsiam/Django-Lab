from django.db import models
from Album.models import Album_Model

class Musician_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    album = models.ForeignKey(Album_Model, on_delete=models.SET_NULL, null=True, blank=True, related_name="musicians")
    instrument_type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
