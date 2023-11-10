from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='movies_list'),
    path('<str:cat>/', views.catalog_ditail_view),
    path('<int:mov_id>/<str:cat>/', views.movi_ditail_view)
]
