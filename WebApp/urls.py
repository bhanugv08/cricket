
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('th/',views.THNQ),
    path('tm/',views.cricketteams),
    path('player/',views.PlayerHistory),
    path('tlist/',views.TeamList),
    path('plist/',views.Playerlist),
    path('matches/',views.MatchesHistory),
]