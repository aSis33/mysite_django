from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postmovie
from .forms import Postform
import os, fnmatch
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def Movie_Post_List(request):
    posts = Postmovie.objects.filter(Published_date__lte = timezone.now()).order_by('-Published_date') ##Displaying posted movie by admin accroding to the published date
    stuff_for_frontend = {'posts':posts}
    return render(request, 'Movie_Management_System/Movie_Post_List.html', stuff_for_frontend)

def Movie_detail(request,pk):
    post = Postmovie.objects.filter(Published_date__lte = timezone.now()).order_by('-Published_date')##EITHER gets specific object from primary key or return 404
    stuff_for_frontend = {'all': post}
    return render(request, 'Movie_Management_System/Movie_details.html',stuff_for_frontend) #render movie details

def Movie(request):
    postie = Postmovie.objects.all()
    context = {"all": postie}
    return render(request, 'Movie_Management_System/Movie.html', context)

def PostV(request):
    #on Post request it will do this
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES) #Fill out the from based on the input information
        if form.is_valid():
            Postmovie = form.save(commit=False)
            Postmovie.Published_date = timezone.now()
            Postmovie.save()
            return redirect('Movie_detail', pk= Postmovie.pk)
    else:
    # on Get request this code is used
        form = Postform()
        context = {"form": form}
    return render(request,'Movie_Management_System/Post_Edit.html', {"form": form})