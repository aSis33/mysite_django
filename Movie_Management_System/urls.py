from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000
    path('', views.Movie_Post_List, name="movie_post_list"),
    path('<int:pk>', views.Movie_detail.as_view(), name="Movie_detail"),
    path('post/new/', views.PostV, name="PostV"),
    path('post/<int:pk>/edit/', views.edit_post, name="POST_EDIT"),
]