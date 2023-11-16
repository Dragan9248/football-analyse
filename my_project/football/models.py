from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    club = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(max_length=50)
    dominant_foot = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=4, decimal_places=2)  # Например, 1.80 метра
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Например, 75.50 кг

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Match(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()
    goal_scorers = models.ManyToManyField(Player, related_name='goals', blank=True)
    assist_providers = models.ManyToManyField(Player, related_name='assists', blank=True)
    yellow_cards = models.PositiveIntegerField()
    red_cards = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.home_team} vs. {self.away_team} - {self.date}"
