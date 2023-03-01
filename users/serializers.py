from rest_framework import serializers
from .models import Profile
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("email", "username", "password")


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
