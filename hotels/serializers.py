from rest_framework import serializers

from hotels.models import Distance, Hotel, HotelAmenity, HotelPhoto, Rule, VacationType


class VacationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationType
        fields = ["id", "name"]


class DistanceSerializer(serializers.ModelSerializer):
    """Расстояния."""

    class Meta:
        model = Distance
        exclude = ("hotel",)


class HotelAmenitySerializer(serializers.ModelSerializer):
    """Удобства."""

    class Meta:
        model = HotelAmenity
        exclude = ("hotel",)


class RuleSerializer(serializers.ModelSerializer):
    """Правила."""

    class Meta:
        model = Rule
        exclude = ("hotel",)


class HotelPhotoSerializer(serializers.ModelSerializer):
    """Фотографии."""

    class Meta:
        model = HotelPhoto
        exclude = ("hotel",)


class HotelSerializer(serializers.ModelSerializer):
    """Отели."""

    amenities = HotelAmenitySerializer(many=True, required=False)
    rules = RuleSerializer(many=True, required=False)
    distances = DistanceSerializer(many=True, required=False)
    photos = HotelPhotoSerializer(many=True, required=False)
    vacation_type = serializers.PrimaryKeyRelatedField(
        queryset=VacationType.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Hotel
        fields = [
            "id",
            "name",
            "vacation_type",
            "hotel_type",
            "category",
            "country",
            "city",
            "address",
            "latitude",
            "longitude",
            "check_in_time",
            "check_out_time",
            "description",
            "amenities",
            "rules",
            "distances",
            "photos",
        ]

    def create(self, validated_data):
        amenities_data = validated_data.pop("amenities", [])
        rules_data = validated_data.pop("rules", [])
        distances_data = validated_data.pop("distances", [])
        photos_data = validated_data.pop("photos", [])

        hotel = Hotel.objects.create(**validated_data)

        for amenity in amenities_data:
            HotelAmenity.objects.create(hotel=hotel, **amenity)
        for rule in rules_data:
            Rule.objects.create(hotel=hotel, **rule)
        for distance in distances_data:
            Distance.objects.create(hotel=hotel, **distance)
        for photo in photos_data:
            HotelPhoto.objects.create(hotel=hotel, **photo)

        return hotel

    def update(self, instance, validated_data):
        amenities_data = validated_data.pop("amenities", None)
        rules_data = validated_data.pop("rules", None)
        distances_data = validated_data.pop("distances", None)
        photos_data = validated_data.pop("photos", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Полная замена вложенных объектов
        if amenities_data is not None:
            instance.amenities.all().delete()
            for amenity in amenities_data:
                HotelAmenity.objects.create(hotel=instance, **amenity)
        if rules_data is not None:
            instance.rules.all().delete()
            for rule in rules_data:
                Rule.objects.create(hotel=instance, **rule)
        if distances_data is not None:
            instance.distances.all().delete()
            for distance in distances_data:
                Distance.objects.create(hotel=instance, **distance)
        if photos_data is not None:
            instance.photos.all().delete()
            for photo in photos_data:
                HotelPhoto.objects.create(hotel=instance, **photo)

        return instance
