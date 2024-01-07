from django.shortcuts import render

from movieapp.forms import Movie_ModelForm
from movieapp.models import Movie


# Create your views here.
def movie_form(request):
    form = Movie_ModelForm()
    if request.method == 'POST':
        form = Movie_ModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
            form = Movie_ModelForm()
            return index_view(request)
    return render(request, 'movieapp/movieform.html', {'form': form})


def list_movie_view(request):
    movies = Movie.objects.all()
    return render(request, 'movieapp/listmovie.html', {'movies': movies})


def index_view(request):
    return render(request, 'movieapp/index.html')
