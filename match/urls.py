from django.contrib import admin
from django.urls import path, include
from .views import getAll, getMatch

urlpatterns = [
    path("", getAll, name="getAll"),
    path("<int:id>", getMatch, name="getMatch"),
]
