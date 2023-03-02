from django.shortcuts import render
from .serializers import MerchandiseSerializer
from rest_framework.decorators import api_view
from .models import merchandise
from django.http import JsonResponse


@api_view(["GET"])
def getMerchandise(request):
    merch = merchandise.objects.all()
    serializer = MerchandiseSerializer(merch, many=True)
    return JsonResponse(serializer.data, safe=False)
