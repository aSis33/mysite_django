from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postmovie
# Create your views here.
def Movie_Post_List(request):
    posts = Postmovie.objects.filter(Published_date__lte = timezone.now()).order_by('-Published_date') ##Displaying posted movie by admin accroding to the published date
    stuff_for_frontend = {'posts':posts}
    return render(request, 'Movie_Management_System/Movie_Post_List.html', stuff_for_frontend)

def Movie_detail(request, pk):
    post = get_object_or_404(Postmovie, pk=pk) ##EITHER gets specific object from primary key or return 404
    stuff_for_frontend = {'post': post}
    return render(request, 'Movie_Management_System/Movie_details.html',stuff_for_frontend) #render movie details