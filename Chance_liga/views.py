from django.shortcuts import render
from . models import Team, Chart, Player
from django.http import HttpResponseNotFound

def domu(request):
    return render(request, 'domu.html') # render je funkce, která slouží k vykreslení HTML šablony na základě zadaných dat

def seznam_tymu(request):
    teams = Team.objects.all()
    return render(request, 'seznam_tymu.html', {'teams': teams})

def tabulka(request):
    teams = Chart.objects.all()
    return render(request, 'tabulka.html', {'teams': teams})

def soupiska_hracu(request,team_id):
    try:
        players = Player.objects.all() # Získání všech hráčů pro tento tým
        team = Team.objects.get(id=team_id) # vrací tým na který kliknu, podle id
        return render(request, 'soupiska_hracu.html', {'team': team, 'players': players})
    except:
        return HttpResponseNotFound('<h1>Tým s tímto ID neexistuje</h1>')