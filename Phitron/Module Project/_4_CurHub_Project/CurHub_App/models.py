from django.db import models
from django.contrib.auth.models import User

from Brand_App.models import Brand

class Car(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car', null=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='CurHub_App/img/cars')
    quantity = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} ({self.year})"



class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment_text = models.TextField()
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text[:50]
    
class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)