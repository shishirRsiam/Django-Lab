from django.urls import path
from . import views
urlpatterns = [
    path('form/',views.home,name='home_page'),
]
