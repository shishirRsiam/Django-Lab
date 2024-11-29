from django.contrib.auth.models import User
from django.db import models

class UserAccount(models.Model):
    balance = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)
    
    created_at = models.DateTimeField(auto_now_add=True, null=1)
    updated_at = models.DateTimeField(auto_now=True, null=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return f"{self.user.username}'s profile"

class nextForeignKey(models.Model):
    balance = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)
    
    created_at = models.DateTimeField(auto_now_add=True, null=1)
    updated_at = models.DateTimeField(auto_now=True, null=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test')

    def __str__(self):
        return f"{self.user.username}'s profile"

