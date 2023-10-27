from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound

# Create your views here.
CATEGORIES = (
    'action',
    'camedy',
    'tv_shows',
)


def index(request):
    return HttpResponse('<h3>Main page</h3>')


def catalog_view(request):
    if request.GET:
        params = request.GET
        id_ = params.get('movi_id')
        print(id_)
    return HttpResponse('<h3>Main page</h3>actions</p>TV shows</p>')


def catalog_ditail_view(request, cat):
    if cat not in CATEGORIES:
        return redirect('/', permanent=True)
    return HttpResponse(f'<h3>Main page</h3></p>{cat}</p>')


def movi_ditail_view(request, cat, movi_id):
    return HttpResponse(f'<h3>{cat}</h3></p>{movi_id}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h3>Hello world</h3>')
