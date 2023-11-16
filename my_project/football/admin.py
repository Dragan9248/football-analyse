# football/admin.py

from django.contrib import admin
from .models import Team, Player, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'club', 'position', 'nationality', 'date_of_birth', 'dominant_foot', 'height', 'weight')
    list_filter = ('club', 'position', 'nationality', 'dominant_foot')
    search_fields = ('first_name', 'last_name', 'club__name')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'home_team', 'away_team', 'home_team_score', 'away_team_score', 'location', 'yellow_cards', 'red_cards')
    list_filter = ('home_team', 'away_team', 'date', 'location')
    search_fields = ('home_team__name', 'away_team__name')

