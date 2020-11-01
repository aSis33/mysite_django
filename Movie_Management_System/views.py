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
            localpost.Published_date = timezone.now()
            localpost.save()

            return redirect('Movie_detail', pk=localpost.pk)
    else:
        # on Get request this code is used
        form = Postform()
    return render(request, 'Movie_Management_System/Post_Edit.html', {"form": form})


def edit_post(request, pk):
    # on Post request it will do this
    localpost = get_object_or_404(Postmovie, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES,
                        instance=localpost)  # Fill out the from based on the input information
        if form.is_valid():
            localpost = form.save(commit=False)
            localpost.Published_date = timezone.now()
            localpost.save()
            return redirect('Movie_detail', pk=localpost.pk)
    else:
        # on Get request this code is used
        form = Postform()
    return render(request, 'Movie_Management_System/Post_Edit.html', {"form": form})
