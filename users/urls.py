from django.urls import include, path
from .views import UserAPIView, createAvatar

app_name = "users"

urlpatterns = [
    path("profile/", UserAPIView.as_view(), name="all-profiles"),
    # path("profile/<int:pk>/", userProfileDetailView.as_view(), name="profile"),
    path("create-avatar", createAvatar, name="create-avatar"),
]
