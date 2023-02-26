from django.contrib import admin
from django.urls import path, include
from .views import getAll

urlpatterns = [path("", getAll, name="getAll")]
