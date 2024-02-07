from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name=''),
    path('payment', views.ptraining, name='ptraining'),
    path('getdata', views.about, name='about'),
]