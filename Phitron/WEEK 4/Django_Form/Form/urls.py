from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.homes),
    path('contact/', views.contact),
    path('about/', views.about),
    path('services/', views.services),
    path('login/', views.login),
]
