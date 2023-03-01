from rest_framework import serializers
from .models import Profile, Avatar
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("email", "username", "password")


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    balance = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    rarity = serializers.SerializerMethodField()

    def get_balance(self, obj):
        profile = Profile.objects.get(user=obj)
        return profile.balance

    def get_level(self, obj):
        profile = Profile.objects.get(user=obj)
        return profile.level

    def get_rarity(self, obj):
        profile = Profile.objects.get(user=obj)
        return profile.rarity

    class Meta:
        model = Profile
        fields = [
            "user",
            "age",
            "dob",
            "name",
            "favourite_team",
            "favourite_player",
            "balance",
            "level",
            "rarity",
        ]


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = "__all__"
