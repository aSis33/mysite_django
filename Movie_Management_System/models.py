from django.db import models

# Create your models here.
class Postmovie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_file = models.FileField(upload_to="media/movies")
    release_date = models.DateField(blank=True, null=True)
    Director_Name = models.CharField(max_length=100)
    Actors_Name = models.CharField(max_length=100)
    Published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):  ##This reutrn title name while in shell or in admin interface
        return self.movie_title
