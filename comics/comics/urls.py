from django.urls import path
from comics import views

urlpatterns=[
    path('searchComics', views.results, name="results"),
    path('searchComics/comics', views.comics, name='comics'),
    path('searchComics/comics/<title>',views.comics, name='comics'),
    path('searchComics/personajes', views.personajes, name='personajes'),
    path('searchComics/personajes/<name>',views.personajes, name='personajes'),
]