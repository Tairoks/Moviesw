from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from catalog.models import Movie

# Create your views here.
CATEGORIES = (
    'action',
    'camedy',
    'tv_shows',
)


def index(request):
    return render(request, 'base.html')


def catalog_view(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies
    }
    return render(request, "movies.html", context=context)


def catalog_detail_view(request, cat):
    if cat not in CATEGORIES:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h3>Main page</h3></p>{cat}</p>')


def movi_detail_view(request, cat, movi_id):
    return HttpResponse(f'<h3>{cat}</h3></p>{movi_id}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h3>Page not found</h3>')
