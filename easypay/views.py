from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
import requests
import time
mc_url="https://api.thingspeak.com/update?api_key=8R3CO2HRXMICK3VK&field1="

def hi(request):
    products = Products.objects.all().values()
    template = loader.get_template('landpage.html')
    context = {
    'products': products,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    context ={}
    return HttpResponse(template.render(context, request))

def ptraining(request):
    template = loader.get_template('ptraining.html')
    context ={}
    return HttpResponse(template.render(context, request))
