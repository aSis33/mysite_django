from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Postmovie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_file = models.FileField(upload_to="media")
    release_date = models.DateField(blank=True, null=True)
    Director_Name = models.CharField(max_length=100)
    Actors_Name = models.CharField(max_length=100)
    Published_date = models.DateTimeField(blank=True, null=True)
    Thumbnail = models.ImageField(upload_to="media/gallery", null=False)

    def publish(self):
        self.Published_date = timezone.now()
        self.save()

    def __str__(self):   ##returns the title in the shell
        return self.movie_title

    def get_absolute_url(self): ## using get_absolute_url to redirect to detail page from search engine
        return reverse('Movie_detail', args=[self.id,])


