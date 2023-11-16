# football/views.py

from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Match

def index(request):
    return render(request, 'index.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'player_detail.html', {'player': player})

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match_list.html', {'matches': matches})

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'match_detail.html', {'match': match})
