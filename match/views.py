from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Match
from .serializers import MatchSerializer


# Create your views here.
def getAll(request):
    if request.method == "GET":
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return JsonResponse(serializer.data, safe=False)
    
def getMatch(request, id):
    if request.method == "GET":
        match = Match.objects.get(id=id)
        serializer = MatchSerializer(match)
        return JsonResponse(serializer.data, safe=False)
