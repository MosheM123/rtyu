from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name=''),
    path('ptraining', views.ptraining, name='ptraining'),
    path('about', views.about, name='about'),
]
