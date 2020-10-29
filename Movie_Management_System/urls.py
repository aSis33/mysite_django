from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000
    path('', views.Movie_Post_List, name="movie_post_list"),
    path('post/<int:pk>/', views.Movie_detail, name="Movie_detail"),
    path('post/watch/', views.Movie, name="Movie_watch"),
    path('post/new/', views.PostV, name="PostV")
]