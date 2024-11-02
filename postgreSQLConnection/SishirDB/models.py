from django.db import models
from django.shortcuts import render
from django.http import HttpResponse

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class MealDetails(models.Model):
    meal_name = models.CharField(max_length=255)
    meal_description = models.TextField()
    

def home(request):
    return HttpResponse("This is Home...")

def saveData(request):
    return HttpResponse("User saved successfully!")

def saveDatas(request):
    # Static data for user
    static_username = "Sishir Siam"
    static_email = "shishir.siam@gmail.com"
    static_age = 21

    # Create a new user instance
    user = User(username=static_username, email=static_email, age=static_age)

    try:
        user.save() 
        return HttpResponse("User saved successfully!")
    except Exception as e:
        return HttpResponse(f"Error saving user: {e}")
