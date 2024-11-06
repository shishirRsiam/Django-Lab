from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=201, null=True)
    phone = models.CharField(max_length=18, null=True)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
