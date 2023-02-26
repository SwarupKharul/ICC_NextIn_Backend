from rest_framework import serializers

from .models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "date",
            "time",
            "home_team",
            "away_team",
            "home_team_logo",
            "away_team_logo",
            "venue",
            "title",
        )
