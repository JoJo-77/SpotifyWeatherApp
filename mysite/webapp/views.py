from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import zipform
from .get_weather import *

# Create your views here.
# Command if you accidently ctrl+z instead of ctrl+c 
# sudo lsof -t -i tcp:8000 | xargs kill -9
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
        try:
            weather_dict = get_data((request.POST.get('zipcode')))
            weather_dict = get_mood(weather_dict)
            print("zip: " + str(request.POST.get('zipcode')))
            print("weather: ", weather_dict['weather'])
            if weather_dict["mood"] is not None:
                mood += weather_dict['mood'] +".html"
            else:
                weather_dict["mood"] = "sunny.html"
        except:
            print("issue finding zipcode")
            mood = "home.html"
    else:
        form = zipform()
        mood = "home.html"
    return render(request,mood, {'form':form})

