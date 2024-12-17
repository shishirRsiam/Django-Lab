from django.urls import path
from .views import api_home

urlpatterns = [
    path('api/home/', api_home, name='api-home'),
]
