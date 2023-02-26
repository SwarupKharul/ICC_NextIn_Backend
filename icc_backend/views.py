from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index(request):
    response = {
        "status": "success",
        "message": "Welcome",
    }
    return JsonResponse(response)
