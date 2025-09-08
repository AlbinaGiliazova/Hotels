from django.contrib import admin

from rooms.models import Amenity, Room, RoomPhoto, Rule


class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1  # Показывать 1 пустую строку для ввода


class RuleInline(admin.TabularInline):
    model = Rule
    extra = 1


class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "room_type", "meal_type", "adults", "children", "area", "quantity")
    inlines = [AmenityInline, RuleInline, RoomPhotoInline]
    search_fields = ("id",)
    list_filter = ("room_type", "meal_type")


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "amenity_type", "room")
    list_filter = ("amenity_type",)
    search_fields = ("name",)


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "room", "rule_choice")
    list_filter = ("rule_choice",)
    search_fields = ("name",)


@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "description")
    search_fields = ("description",)
