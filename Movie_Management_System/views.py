from django.shortcuts import render
from django.utils import timezone
from .models import Postmovie
# Create your views here.
def Movie_Post_List(request):
    posts = Postmovie.objects.filter(Published_date__lte = timezone.now()).order_by('-Published_date') ##Displaying posted movie by admin accroding to the published date
    stuff_for_frontend = {'posts':posts}
    return render(request, 'Movie_Management_System/Movie_Post_List.html', stuff_for_frontend)