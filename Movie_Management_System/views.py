from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView
from .models import Postmovie, Comment
from .forms import Postform, RegistrationForm, LoginForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

@login_required
def PostV(request):
    # on Post request it will do this

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)  # Fill out the from based on the input information
        if form.is_valid():
            localpost = form.save(commit=False)
            localpost.Publisher = request.user
            # localpost.Published_date = timezone.now() ##we set publish time on below publish post function
            localpost.save()

            return redirect('Movie_detail', pk=localpost.pk)
    else:
        # on Get request this code is used
        form = Postform()
    return render(request, 'Movie_Management_System/Post_Edit.html', {"form": form})

#function to edit a post
@login_required
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
@login_required
def Post_draft(request):
    post = Postmovie.objects.filter(Published_date__isnull=True).order_by('-release_date')
    return render(request, 'Movie_Management_System/draft_list.html', {'post': post})

#view for post
@login_required
def publish_post(request, pk):
    post = get_object_or_404(Postmovie, pk=pk)
    post.publish()  # This publish method is already created in model.py
    return redirect('Movie_detail', pk=pk)

#view for delete
@login_required
def delete_movies(request, pk):
    movie = Postmovie.objects.get(pk=pk)
    movie.delete()
    return redirect('movie_post_list')

def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('LOGIN')
        else:
            return HttpResponse("READ CRITERIA OF FORM")

    else:
        user_form = RegistrationForm()
        return render(request, 'Movie_Management_System/registration.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data ##cd = cleaned data
            user= authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('movie_post_list')
                else:
                    return HttpResponse("<h1>BAD INPUT</h1>")

            else:
                return HttpResponse("<h1> Invalid login </h1>")
    else:
        form = LoginForm()
        return render(request,"Movie_Management_System/login.html", {"form":form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('movie_post_list')


def show_list(request):
    query = None
    results = []
    if request.method == "GET":
        query=request.GET.get("search")
        results=Postmovie.objects.filter(Q(movie_title__icontains=query) | Q(movie_description__icontains=query))
        

    return render(request,"Movie_Management_System/search_list.html",{'query':query,'results':results})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Postmovie, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect("Movie_detail", pk=post.pk) ##redirecting to the that movie detail after commenting
    else:
        form = CommentForm()
    return render(request,"Movie_Management_System/add_comment_to_post.html",{'form':form})

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('Movie_detail', pk=comment.post.pk) ##digging into the post and that post primary key