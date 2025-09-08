from rest_framework import viewsets

from rooms.models import Amenity, Room, RoomPhoto, Rule
from rooms.serializers import AmenitySerializer, RoomPhotoSerializer, RoomSerializer, RuleSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """Номера."""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    """Удобства номеров."""

    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class RuleViewSet(viewsets.ModelViewSet):
    """Правила номеров."""

    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class RoomPhotoViewSet(viewsets.ModelViewSet):
    """Фотографии номеров."""

    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
