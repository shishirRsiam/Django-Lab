from django.db import models

class Album_Model(models.Model):
    name = models.CharField(max_length=100)
    album_release_date = models.DateField(auto_now_add=True)

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    Rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self) -> str:
        return self.name
