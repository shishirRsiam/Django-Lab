from django.db import models
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'