"""Сериализаторы приложения."""

from rest_framework import serializers

from meals.models import MealType


class MealTypeSerializer(serializers.ModelSerializer):
    """Сериализатор типа питания."""

    class Meta:
        model = MealType
        fields = ["type", "price"]
