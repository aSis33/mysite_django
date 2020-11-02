from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000
    path('', views.Movie_Post_List, name="movie_post_list"),
    #127.0.0.1:8000/2
    path('<int:pk>', views.Movie_detail.as_view(), name="Movie_detail"),
    # 127.0.0.1:8000/post/new
    path('post/new/', views.PostV, name="PostV"),
    # 127.0.0.1:8000/2/edit
    path('<int:pk>/edit/', views.edit_post, name="POST_EDIT"),
    # 127.0.0.1:8000/draft
    path('draft/', views.Post_draft, name="Post_Draft"),

    path('<int:pk>/publish/', views.publish_post, name="Post_Publish"),

    path('<int:pk>/delete/', views.delete_movies, name="Delete"),
]