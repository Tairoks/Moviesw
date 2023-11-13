from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='movies_list'),
    path('<str:cat>/', views.catalog_detail_view),
    path('<int:mov_id>/<str:cat>/', views.movi_detail_view)
]

# urlpatterns = [
#     path('', views.catalog_view, name='movies_list'),
#     path('<slug:actor_slug>/', views.catalog_detail_view),
#     path('<str:cat>/<int:mov_id>/', views.movie_detail_view),
# ]