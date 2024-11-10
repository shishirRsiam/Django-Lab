from django.contrib import admin
from django.urls import path
from . import views

from Task import views as TaskViews
from Category import views as CategoryViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskViews.show_task, name='home'),
    path('task/add', TaskViews.add_task, name='add_task'),
    path('task/edit/<int:id>', TaskViews.edit_task, name='edit_task'),
    path('task/delete/<int:id>', TaskViews.delete_task, name='delete_task'),
    path('category/add', CategoryViews.add_category, name='add_category'),
]
