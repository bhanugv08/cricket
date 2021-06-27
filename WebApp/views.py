from django.shortcuts import render,redirect
from .forms import TeamForm,PlayerForm,MatchesForm
from WebApp.models import Team,Player
import datetime
from datetime import datetime
from django.http import HttpResponseRedirect

def THNQ(request):
    return render(request,'MyApp/thanks.html')

def Home(request):
    return render(request,'MyApp/home.html')

def cricketteams(request):

    if request.method=='POST':
        form=TeamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
    else:
        form=TeamForm()
    return render(request,'MyApp/teams.html',{'form':form})

def TeamList(request):
    obj=Team.objects.all()
    return  render(request,'MyApp/teamlist.html',{'obj':obj})

def PlayerHistory(request):
    if request.method=='POST':
        form=PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
    else:
        form=PlayerForm()
    return render(request,'MyApp/player.html',{'form':form})

def Playerlist(request):
    obj=Player.objects.all()
    return render(request,'Myapp/playerlist.html',{'obj':obj})



def MatchesHistory(request):
    if request.method=='POST':
        form=MatchesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/th/')
    else:
        form=MatchesForm()
    return render(request,'MyApp/matches.html',{'form':form})




