from rest_framework import serializers

from rooms.models import Amenity, MealType, Room, RoomPhoto, Rule


class AmenitySerializer(serializers.ModelSerializer):
    """Удобства номера."""

    class Meta:
        model = Amenity
        fields = ["id", "amenity_type", "name"]


class RuleSerializer(serializers.ModelSerializer):
    """Правила номера."""

    class Meta:
        model = Rule
        fields = ["id", "name", "rule_choice"]


class RoomPhotoSerializer(serializers.ModelSerializer):
    """Фотографии номера."""

    class Meta:
        model = RoomPhoto
        fields = ["id", "image", "description"]


class RoomSerializer(serializers.ModelSerializer):
    """Номер."""

    amenities = AmenitySerializer(many=True, required=False)
    rules = RuleSerializer(many=True, required=False)
    photos = RoomPhotoSerializer(many=True, required=False)
    meal_type = serializers.PrimaryKeyRelatedField(queryset=MealType.objects.all(), allow_null=True)

    class Meta:
        model = Room
        fields = [
            "id",
            "room_type",
            "meal_type",
            "adults",
            "children",
            "area",
            "quantity",
            "double_bed",
            "single_bed",
            "amenities",
            "rules",
            "photos",
        ]

    def create(self, validated_data):
        amenities_data = validated_data.pop("amenities", [])
        rules_data = validated_data.pop("rules", [])
        photos_data = validated_data.pop("photos", [])
        room = Room.objects.create(**validated_data)
        for amenity in amenities_data:
            Amenity.objects.create(room=room, **amenity)
        for rule in rules_data:
            Rule.objects.create(room=room, **rule)
        for photo in photos_data:
            RoomPhoto.objects.create(room=room, **photo)
        return room

    def update(self, instance, validated_data):
        amenities_data = validated_data.pop("amenities", None)
        rules_data = validated_data.pop("rules", None)
        photos_data = validated_data.pop("photos", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if amenities_data is not None:
            # Сначала удаляем старые, потом создаём новые
            Amenity.objects.filter(room=instance).delete()
            for amenity in amenities_data:
                Amenity.objects.create(room=instance, **amenity)

        if rules_data is not None:
            Rule.objects.filter(room=instance).delete()
            for rule in rules_data:
                Rule.objects.create(room=instance, **rule)

        if photos_data is not None:
            RoomPhoto.objects.filter(room=instance).delete()
            for photo in photos_data:
                RoomPhoto.objects.create(room=instance, **photo)
        return instance
