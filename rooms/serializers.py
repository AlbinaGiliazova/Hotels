from rest_framework import serializers

from rooms.models import (
    BathroomAmenities,
    Bed,
    CustomBathroomAmenities,
    CustomDrinkingAmenities,
    CustomGeneralAmenities,
    CustomViewAmenities,
    DrinkingAmenities,
    GeneralAmenities,
    Room,
    ViewAmenities,
)


class BedSerializer(serializers.ModelSerializer):
    """Кровати."""

    class Meta:
        model = Bed
        fields = [
            "id",
            "has_single",
            "single_quantity",
            "has_double",
            "double_quantity",
        ]


class GeneralAmenitiesSerializer(serializers.ModelSerializer):
    """Общие удобства."""

    class Meta:
        model = GeneralAmenities
        exclude = ("room",)


class DrinkingAmenitiesSerializer(serializers.ModelSerializer):
    """Напитки."""

    class Meta:
        model = DrinkingAmenities
        exclude = ("room",)


class BathroomAmenitiesSerializer(serializers.ModelSerializer):
    """Ванная комната."""

    class Meta:
        model = BathroomAmenities
        exclude = ("room",)


class ViewAmenitiesSerializer(serializers.ModelSerializer):
    """Вид."""

    class Meta:
        model = ViewAmenities
        exclude = ("room",)


class CustomGeneralAmenitiesSerializer(serializers.ModelSerializer):
    """Дополнительные общие удобства."""

    class Meta:
        model = CustomGeneralAmenities
        exclude = ("room",)


class CustomBathroomAmenitiesSerializer(serializers.ModelSerializer):
    """Дополнительные удобства в ванной комнате."""

    class Meta:
        model = CustomBathroomAmenities
        exclude = ("room",)


class CustomViewAmenitiesSerializer(serializers.ModelSerializer):
    """Дополнительные удобства вида."""

    class Meta:
        model = CustomViewAmenities
        exclude = ("room",)


class CustomDrinkingAmenitiesSerializer(serializers.ModelSerializer):
    """Дополнительные удобства напитков."""

    class Meta:
        model = CustomDrinkingAmenities
        exclude = ("room",)


class RoomSerializer(serializers.ModelSerializer):
    """Сериализатор номеров."""

    beds = BedSerializer()
    general_amenities = GeneralAmenitiesSerializer(many=True, source="generalamenities_set", required=False)
    drinking_amenities = DrinkingAmenitiesSerializer(many=True, source="drinkingamenities_set", required=False)
    bathroom_amenities = BathroomAmenitiesSerializer(many=True, source="bathroomamenities_set", required=False)
    view_amenities = ViewAmenitiesSerializer(many=True, source="viewamenities_set", required=False)
    custom_general_amenities = CustomGeneralAmenitiesSerializer(
        many=True, source="customgeneralamenities_set", required=False
    )
    custom_drinking_amenities = CustomDrinkingAmenitiesSerializer(
        many=True, source="customdrinkingamenities_set", required=False
    )
    custom_bathroom_amenities = CustomBathroomAmenitiesSerializer(
        many=True, source="custombathroomamenities_set", required=False
    )
    custom_view_amenities = CustomViewAmenitiesSerializer(many=True, source="customviewamenities_set", required=False)

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
            "beds",
            "general_amenities",
            "drinking_amenities",
            "bathroom_amenities",
            "view_amenities",
            "custom_general_amenities",
            "custom_drinking_amenities",
            "custom_bathroom_amenities",
            "custom_view_amenities",
        ]

    def create(self, validated_data):
        beds_data = validated_data.pop("beds")
        general_amenities_data = validated_data.pop("generalamenities_set", [])
        drinking_amenities_data = validated_data.pop("drinkingamenities_set", [])
        bathroom_amenities_data = validated_data.pop("bathroomamenities_set", [])
        view_amenities_data = validated_data.pop("viewamenities_set", [])
        custom_general_amenities_data = validated_data.pop("customgeneralamenities_set", [])
        custom_drinking_amenities_data = validated_data.pop("customdrinkingamenities_set", [])
        custom_bathroom_amenities_data = validated_data.pop("custombathroomamenities_set", [])
        custom_view_amenities_data = validated_data.pop("customviewamenities_set", [])

        bed = Bed.objects.create(*beds_data)
        room = Room.objects.create(beds=bed, **validated_data)

        for amenity_data in general_amenities_data:
            GeneralAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in drinking_amenities_data:
            DrinkingAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in bathroom_amenities_data:
            BathroomAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in view_amenities_data:
            ViewAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in custom_general_amenities_data:
            CustomGeneralAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in custom_drinking_amenities_data:
            CustomDrinkingAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in custom_bathroom_amenities_data:
            CustomBathroomAmenities.objects.create(room=room, **amenity_data)
        for amenity_data in custom_view_amenities_data:
            CustomViewAmenities.objects.create(room=room, **amenity_data)

        return room
