import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import zipform
from .get_weather import *
from .spotbackend import *

# Create your views here.
# Command if you accidently ctrl+z instead of ctrl+c 
# sudo lsof -t -i tcp:8000 | xargs kill -9
# omg that's too funny
weather_dict  = {}
track_list = {}

class to_string:
    pass

def home(request):
    weather_dict = {}
    mood = ""
    if request.method == 'POST':
        form = zipform(request.POST)
        print(request.POST)
        if form.is_valid():
            pass
        try:
            weather_dict = get_data((request.POST.get('zipcode')))
            print(weather_dict)
            weather_dict = get_mood(weather_dict)
            print(weather_dict)
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
    weather_dict['form'] = form
    return render(request,mood,context = weather_dict)

def sunnySong(request):
    return render(request, 'sunnySong.html', context = weather_dict)

def rainySong(request):
    return render(request, 'rainySong.html', context = weather_dict)

def cloudySong(request):
    return render(request, 'cloudySong.html', context = weather_dict)

def windySong(request):
    return render(request, 'windySong.html', context = weather_dict)

def sunny(request):
    return render(request, 'sunny.html',context = weather_dict)

def rainy(request):
    return render(request, 'rainy.html')

def cloudy(request):
    return render(request, 'cloudy.html', context = weather_dict)

def windy(request):
    return render(request, 'windy.html')

def homeSong(request):
    weather_dict = {}
    trackString = ""
    trackToDict = {}
    track_dict = {}
    track_list = {}
    track = {}
    mood = ""
    if request.method == 'POST':
        form = zipform(request.POST)
        print(request.POST)
        if form.is_valid():
            pass
        try:
            weather_dict = get_data((request.POST.get('zipcode')))
            print(weather_dict)
            weather_dict = get_mood(weather_dict)
            print(weather_dict)
            print("zip: " + str(request.POST.get('zipcode')))
            print("weather: ", weather_dict['weather'])
            track = get_tracks(weather_dict)
            trackString = json.dumps(track['spotify'])
            trackString = trackString.replace("https://open.spotify.com/track/", "")
            trackToDict = json.loads(trackString)
            weather_dict['current'] = trackToDict
            if weather_dict["mood"] is not None:
                mood += weather_dict['mood'] +"Song.html"
            else:
                weather_dict["mood"] = "sunnySong.html"
        except Exception as e:
            print(e)
            mood = "homeSong.html"
    else:
        form = zipform()
        mood = "homeSong.html"
    weather_dict['form'] = form
    return render(request,mood,context = weather_dict)