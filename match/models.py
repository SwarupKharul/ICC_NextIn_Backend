from django.db import models


# Create your models here.
class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_team_logo = models.URLField()
    away_team_logo = models.URLField()
    venue = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"{self.title} - {self.home_team} vs {self.away_team}"
