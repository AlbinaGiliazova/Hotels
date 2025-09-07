from rest_framework import mixins, viewsets

from users.models import CustomUser
from users.serializers import RegisterSerializer


class UserViewSet(
    mixins.ListModelMixin,  # GET /api/users/
    mixins.RetrieveModelMixin,  # GET /api/users/<id>/
    mixins.CreateModelMixin,  # POST /api/users/
    viewsets.GenericViewSet,
):
    """Вьюсет регистрации пользователей."""

    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
