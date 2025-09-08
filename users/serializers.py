from django.contrib.auth import get_user_model
from rest_framework import serializers

from food.models import MealType
from hotels.models import Hotel
from rooms.models import Room

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """Регистрация пользователей."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserMealTypeUpdateSerializer(serializers.Serializer):
    """Выбор типа питания."""

    meal_type_id = serializers.PrimaryKeyRelatedField(queryset=MealType.objects.all(), source="meal_type")

    def update(self, instance, validated_data):
        instance.meal_type = validated_data["meal_type"]
        instance.save()
        return instance


class UserHotelSerializer(serializers.ModelSerializer):
    """Выбор отеля."""

    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = ["id", "hotel"]


class UserRoomSerializer(serializers.ModelSerializer):
    """Выбор номера."""

    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = ["id", "room"]
