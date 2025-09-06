"""Вьюсеты приложения."""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from food.models import MealType
from food.serializers import MealTypeSerializer


class MealTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет, возвращающий стоимость типа питания."""

    queryset = MealType.objects.all()
    serializer_class = MealTypeSerializer

    @action(detail=False, methods=["post"], url_path="get_price")
    def get_price(self, request):
        meal_type = request.data.get("type")
        if not meal_type:
            return Response({"error": "Не указан тип питания."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            meal = MealType.objects.get(type=meal_type)
        except MealType.DoesNotExist:
            return Response({"error": "Данный тип питания не найден."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"type": meal.get_type_display(), "price": meal.price})
