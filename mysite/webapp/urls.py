from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home', views.home, name = "home"),
    path('sunny',views.sunny, name = "sunny"),
    path('cloudy',views.cloudy, name = "cloudy"),
    path('rainy',views.rainy, name = "rainy"),
    path('windy',views.windy, name = "windy"),
    path('homeSong', views.homeSong, name="homeSong"),
    path('sunnySong', views.sunnySong, name = "sunnySong"),
    path('cloudySong', views.cloudySong, name = "cloudySong"),
    path('rainySong', views.rainySong, name = "rainySong"),
    path('windySong', views.windySong, name = "windySong"),

]