from django.urls import path
from . import views
urlpatterns = [
    path('form/',views.add_musician,name='add_musician'),
    path('edit/<int:id>',views.edit_musician,name='edit_musician'),
    path('delete/<int:id>',views.delete,name='delete_musician'),
]
