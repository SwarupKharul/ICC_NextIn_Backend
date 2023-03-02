from django.urls import include, path
from .views import getMerchandise

app_name = "store"

urlpatterns = [
    path("merchandise/", getMerchandise, name="merchandise"),
]
