from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Brand_App/img/brands')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name