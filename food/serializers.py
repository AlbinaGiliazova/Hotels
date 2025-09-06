"""Сериализаторы приложения."""

from rest_framework import serializers

from food.models import MealType


class MealTypeSerializer(serializers.ModelSerializer):
    """Сериализатор типа питания."""

    class Meta:
        model = MealType
        fields = ["type", "price"]
