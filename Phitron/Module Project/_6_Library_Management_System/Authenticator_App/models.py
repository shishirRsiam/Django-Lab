from django.db import models
from django.contrib.auth.models import User

class User(User):
    balance = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    