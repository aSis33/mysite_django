from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView
from .models import Postmovie
from .forms import Postform
import os, fnmatch
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def Movie_Post_List(request):
    posts = Postmovie.objects.filter(Published_date__lte=timezone.now()).order_by(
        '-Published_date')  ##Displaying posted movie by admin accroding to the published date
    stuff_for_frontend = {'posts': posts}
    return render(request, 'Movie_Management_System/Movie_Post_List.html', stuff_for_frontend)


class Movie_detail(DetailView):
    # USing generic detail view
    context_object_name = 'obj'
    template_name = 'Movie_Management_System/Movie_details.html'
    model = Postmovie


def PostV(request):
    # on Post request it will do this

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)  # Fill out the from based on the input information
        if form.is_valid():
            localpost = form.save(commit=False)
            # localpost.Published_date = timezone.now() ##we set publish time on below publish post function
            localpost.save()

            return redirect('Movie_detail', pk=localpost.pk)
    else:
        # on Get request this code is used
        form = Postform()
    return render(request, 'Movie_Management_System/Post_Edit.html', {"form": form})

#function to edit a post
def edit_post(request, pk):
    # on Post request it will do this
    localpost = get_object_or_404(Postmovie, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES,
                        instance=localpost)  # Fill out the from based on the input information
        if form.is_valid():
            localpost = form.save(commit=False)
            # localpost.Published_date = timezone.now() ##This line of code is used to set publish time same as edit time
            localpost.save()
            return redirect('Movie_detail', pk=localpost.pk)
    else:
        # on Get request this code is used
        form = Postform()
    return render(request, 'Movie_Management_System/Post_Edit.html', {"form": form})

#function to list those movies which are not published yet
def Post_draft(request):
    post = Postmovie.objects.filter(Published_date__isnull=True).order_by('-release_date')
    return render(request, 'Movie_Management_System/draft_list.html', {'post': post})

#view for post
def publish_post(request, pk):
    post = get_object_or_404(Postmovie, pk=pk)
    post.publish()  # This publish method is already created in model.py
    return redirect('Movie_detail', pk=pk)

#view for delete
def delete_movies(request, pk):
    movie = Postmovie.objects.get(pk=pk)
    movie.delete()
    return redirect('movie_post_list')