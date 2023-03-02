from .models import merchandise
from rest_framework import serializers


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = merchandise
        fields = "__all__"
