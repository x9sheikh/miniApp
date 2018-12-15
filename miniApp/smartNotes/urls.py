
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:notesId>/', views.detailNotes, name='detailNotes'),
    path('createNotes/', views.createNotes, name='createNotes'),

]
