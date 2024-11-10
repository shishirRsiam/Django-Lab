from django.urls import path
from . import views
urlpatterns = [
    path('form/',views.add_album,name='add_album'),
    path('edit/<int:id>',views.edit_album,name='edit_album'),
]
