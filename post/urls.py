from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    
    path('index', views.index, name='post-index'),
    path('create' , views.create , name = 'post-create'),
    path('update/<int:pk>/' , views.update , name = 'post-update'),
    path('user' , views.userpost , name = 'posts-user'),
]