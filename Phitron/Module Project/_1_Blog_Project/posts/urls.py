from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts, name='home'),
    path('add/', views.add_post, name='addpost'),
    path('posts/', views.posts),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>', views.view_post, name='viewpost'),
    path('edit/<int:post_id>', views.edit_post, name='editpost'),
]