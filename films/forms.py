from django import forms
from .models import Reviews, Film

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text']

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'image', 'trailer_url', 'duration']