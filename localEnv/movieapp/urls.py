from django.urls import path
from movieapp import views
from movieapp.views import list_movie_view

urlpatterns = [
    path('', views.index_view,name='index'),
    path('add/', views.movie_form,name='add'),
    path('show/', list_movie_view,name='list')
]
