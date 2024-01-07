from django import forms

from movieapp.models import Movie


class Movie_ModelForm(forms.ModelForm):
    # rdate = forms.DateField()
    # moviename = forms.CharField(max_length=30)
    # hero = forms.CharField(max_length=20)
    # heroine = forms.CharField(max_length=20)
    # rating = forms.IntegerField()

    class Meta:
        model = Movie
        fields = '__all__'
