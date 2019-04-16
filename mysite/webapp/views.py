from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def sunny(request):
    return render(request, 'sunny.html')

def rainy(request):
    return render(request, 'rainy.html')

def cloudy(request):
    return render(request, 'cloudy.html')

def windy(request):
    return render(request, 'windy.html')

