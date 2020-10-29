from django import forms
from .models import Postmovie

class Postform(forms.ModelForm):
    ##using class meta in order to create form according to model
    class Meta:
        model = Postmovie
        fields = ('movie_title','movie_description','movie_file','release_date', 'Director_Name','Actors_Name','Thumbnail')