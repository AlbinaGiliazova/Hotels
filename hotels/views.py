from rest_framework import permissions, viewsets

from .models import Hotel
from .serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    """Вьюсет отелей."""

    queryset = Hotel.objects.all().order_by("name")
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAdminUser]
