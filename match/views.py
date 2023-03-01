from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Match
from .serializers import MatchSerializer
from rest_framework.decorators import api_view


# Create your views here.
def getAll(request):
    if request.method == "GET":
        matches = Match.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def getMatch(request, id):
    match = Match.objects.get(id=id)
    serializer = MatchSerializer(match)
    output = serializer.data
    output["userId"] = request.user.id
    return JsonResponse(output, safe=False)
