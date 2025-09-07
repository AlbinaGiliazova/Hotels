from rest_framework import serializers

from hotels.models import Amenity, Distance, GeneralComfortType, Hotel, HotelPhoto, Rule, VacationType


class HotelPhotoSerializer(serializers.ModelSerializer):
    """Фотографии отеля."""

    class Meta:
        model = HotelPhoto
        fields = ["image", "name"]


class RuleSerializer(serializers.ModelSerializer):
    """Правила отеля."""

    class Meta:
        model = Rule
        fields = ["name", "is_checked", "description"]


class AmenitySerializer(serializers.ModelSerializer):
    """Особые удобства."""

    amenity_type = serializers.PrimaryKeyRelatedField(queryset=Amenity.objects.all())

    class Meta:
        model = Amenity
        fields = ["name", "amenity_type", "is_selected"]


class DistanceSerializer(serializers.ModelSerializer):
    """Расстояния."""

    distance_type = serializers.PrimaryKeyRelatedField(queryset=Distance.objects.all())

    class Meta:
        model = Distance
        fields = ["distance_type", "value"]


class HotelSerializer(serializers.ModelSerializer):
    """Сериализатор отеля."""

    photos = HotelPhotoSerializer(many=True, required=False)
    rules = RuleSerializer(many=True, required=False)
    amenities = AmenitySerializer(many=True, required=False)
    distances = serializers.PrimaryKeyRelatedField(many=True, queryset=Distance.objects.all())
    general_comfort = serializers.PrimaryKeyRelatedField(many=True, queryset=GeneralComfortType.objects.all())
    vacation_type = serializers.PrimaryKeyRelatedField(queryset=VacationType.objects.all())

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
            "distances",
            "general_comfort",
            "check_in_time",
            "check_out_time",
            "description",
            "amenities",
            "rules",
            "photos",
        ]

    def create(self, validated_data):
        photos_data = validated_data.pop("photos", [])
        rules_data = validated_data.pop("rules", [])
        amenities_data = validated_data.pop("amenities", [])

        hotel = Hotel.objects.create(**validated_data)

        # Many-to-Many (distances/general_comfort) автоматически можно добавить через .set() или .add() если не используются вложенные созданные объекты
        if "distances" in self.initial_data:
            hotel.distances.set(validated_data.get("distances", []))
        if "general_comfort" in self.initial_data:
            hotel.general_comfort.set(validated_data.get("general_comfort", []))

        for photo_data in photos_data:
            HotelPhoto.objects.create(hotel=hotel, **photo_data)
        for rule_data in rules_data:
            Rule.objects.create(hotel=hotel, **rule_data)
        for amenity_data in amenities_data:
            Amenity.objects.create(hotel=hotel, **amenity_data)

        return hotel
