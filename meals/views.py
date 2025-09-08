"""Вьюсеты приложения."""

from rest_framework import viewsets

from meals.models import MealType
from meals.serializers import MealTypeSerializer


class MealTypeViewSet(viewsets.ModelViewSet):
    """Вьюсет, возвращающий стоимость типа питания."""

    queryset = MealType.objects.all()
    serializer_class = MealTypeSerializer
