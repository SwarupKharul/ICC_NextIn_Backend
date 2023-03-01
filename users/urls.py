from django.urls import include, path
from .views import UserAPIView, createAvatar, getAvatar, reduceBalance

app_name = "users"

urlpatterns = [
    path("profile/", UserAPIView.as_view(), name="all-profiles"),
    path("create-avatar", createAvatar, name="create-avatar"),
    path("get-avatar", getAvatar, name="get-avatar"),
    path("reduce-balance", reduceBalance, name="reduce-balance")
]
