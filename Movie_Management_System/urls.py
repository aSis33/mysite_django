from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000
    path('', views.Movie_Post_List, name="movie_post_list"),
    #127.0.0.1:8000/post/2(Primary key of movies)
    path('post/<int:pk>/', views.Movie_detail, name="Movie_detail")
]