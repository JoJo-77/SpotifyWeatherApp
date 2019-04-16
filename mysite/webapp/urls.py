from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('sunny',views.sunny, name = "sunny"),
    path('cloudy',views.cloudy, name = "cloudy"),
    path('rainy',views.rainy, name = "rainy"),
    path('windy',views.windy, name = "windy")
]