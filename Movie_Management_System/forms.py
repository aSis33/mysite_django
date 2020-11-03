from django import forms
from .models import Postmovie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Postform(forms.ModelForm):
    ##using class meta in order to create form according to model
    class Meta:
        model = Postmovie
        fields = ('movie_title','movie_description','movie_file','release_date', 'Director_Name','Actors_Name','Thumbnail')

##Creating new form and connecting to UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name','password1','password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

