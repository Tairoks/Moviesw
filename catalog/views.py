from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h3>Main page</h3>')
