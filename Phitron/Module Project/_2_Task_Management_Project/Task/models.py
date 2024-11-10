from django.db import models
from django import forms
from Category.models import Category
import datetime

class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name='tasks')
    taskAssignDate = models.DateField(default=datetime.date.today) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskTitle


class TaskForms(forms.ModelForm):
    # taskAssignDate = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    #     required=True
    # )
    taskAssignDate = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Task
        fields = '__all__'