from django.urls import path
from . import views as Brand_App_Views

urlpatterns = [    
    path('add/brand/', Brand_App_Views.add_brands, name='add_brand'),
]
