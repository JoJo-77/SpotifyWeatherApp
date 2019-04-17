from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import zipform
from .get_weather import *

# Create your views here.

def sunny(request):
    return render(request, 'sunny.html')

def rainy(request):
    return render(request, 'rainy.html')

def cloudy(request):
    return render(request, 'cloudy.html')

def windy(request):
    return render(request, 'windy.html')

def home(request):
    weather_dict = None
    mood = ""
    if request.method == 'POST':
        form = zipform(request.POST)
        if form.is_valid():
            pass
        weather_dict = get_data((request.POST.get('zipcode')))
        weather_dict = get_mood(weather_dict)
        print(weather_dict)
        mood += weather_dict['mood'] +".html"
    else:
        form = zipform()
        mood = "home.html"
    return render(request,mood, {'form':form})

