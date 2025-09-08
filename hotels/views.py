from rest_framework import viewsets

from hotels.serializers import (
    DistanceSerializer,
    HotelAmenitySerializer,
    HotelPhotoSerializer,
    HotelSerializer,
    RuleSerializer,
    VacationTypeSerializer,
)

from .models import Distance, Hotel, HotelAmenity, HotelPhoto, Rule, VacationType


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class VacationTypeViewSet(viewsets.ModelViewSet):
    queryset = VacationType.objects.all()
    serializer_class = VacationTypeSerializer


class DistanceViewSet(viewsets.ModelViewSet):
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer


class HotelAmenityViewSet(viewsets.ModelViewSet):
    queryset = HotelAmenity.objects.all()
    serializer_class = HotelAmenitySerializer


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer
