from django.contrib.auth import get_user_model
from rest_framework import decorators, mixins, permissions, status, viewsets
from rest_framework.response import Response

from users.serializers import (
    RegisterSerializer,
    UserHotelSerializer,
    UserMealTypeUpdateSerializer,
)

User = get_user_model()


class UserViewSet(
    mixins.ListModelMixin,  # GET /api/users/
    mixins.RetrieveModelMixin,  # GET /api/users/<id>/
    mixins.CreateModelMixin,  # POST /api/users/
    viewsets.GenericViewSet,
):
    """Вьюсет регистрации пользователей."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @decorators.action(
        detail=False, methods=["post"], url_path="set-meal-type", permission_classes=[permissions.IsAuthenticated]
    )
    def set_meal_type(self, request):
        serializer = UserMealTypeUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(request.user, serializer.validated_data)
            return Response({"message": "Тип питания обновлён"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(
        detail=True, methods=["post"], url_path="set-hotel", permission_classes=[permissions.IsAuthenticated]
    )
    def set_hotel(self, request, pk=None):
        user = self.get_object()
        serializer = UserHotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(user, serializer.validated_data)
            return Response({"message": "Отель назначен пользователю"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
