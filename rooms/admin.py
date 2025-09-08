from django.contrib import admin

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


@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ("id", "has_single", "single_quantity", "has_double", "double_quantity")
    list_filter = ("has_single", "has_double")
    search_fields = ("id",)


@admin.register(GeneralAmenities)
class GeneralAmenitiesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "wifi",
        "sofa",
        "conditioner",
        "heating",
        "beds",
        "tv",
        "dinnertable",
        "kitchen",
        "worktable",
        "wardrobe",
        "bar",
        "room",
    )
    list_filter = ("wifi", "conditioner", "heating", "kitchen", "tv", "room")
    search_fields = ("name",)


@admin.register(DrinkingAmenities)
class DrinkingAmenitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "teapot", "coffee", "tea", "dishes", "room")
    list_filter = ("teapot", "coffee", "tea", "room")
    search_fields = ("name",)


@admin.register(BathroomAmenities)
class BathroomAmenitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "bath", "shower", "bidet", "jakuzzi", "fan", "bathrobe", "room")
    list_filter = ("bath", "shower", "bidet", "jakuzzi", "fan", "bathrobe", "room")
    search_fields = ("name",)


@admin.register(ViewAmenities)
class ViewAmenitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "sea", "pool", "park", "sight", "room")
    list_filter = ("sea", "pool", "park", "sight", "room")
    search_fields = ("name",)


class CustomAmenitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "is_selected", "room")
    list_filter = ("is_selected", "room")
    search_fields = ("name",)


admin.site.register(CustomGeneralAmenities, CustomAmenitiesAdmin)
admin.site.register(CustomDrinkingAmenities, CustomAmenitiesAdmin)
admin.site.register(CustomBathroomAmenities, CustomAmenitiesAdmin)
admin.site.register(CustomViewAmenities, CustomAmenitiesAdmin)


class GeneralAmenitiesInline(admin.TabularInline):
    model = GeneralAmenities
    extra = 0


class DrinkingAmenitiesInline(admin.TabularInline):
    model = DrinkingAmenities
    extra = 0


class BathroomAmenitiesInline(admin.TabularInline):
    model = BathroomAmenities
    extra = 0


class ViewAmenitiesInline(admin.TabularInline):
    model = ViewAmenities
    extra = 0


class CustomGeneralAmenitiesInline(admin.TabularInline):
    model = CustomGeneralAmenities
    extra = 0


class CustomDrinkingAmenitiesInline(admin.TabularInline):
    model = CustomDrinkingAmenities
    extra = 0


class CustomBathroomAmenitiesInline(admin.TabularInline):
    model = CustomBathroomAmenities
    extra = 0


class CustomViewAmenitiesInline(admin.TabularInline):
    model = CustomViewAmenities
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "room_type",
        "meal_type",
        "adults",
        "children",
        "area",
        "quantity",
        "beds",
    )
    list_filter = (
        "room_type",
        "meal_type",
        "adults",
        "children",
        "area",
        "quantity",
        "beds",
    )
    search_fields = ("id",)
    inlines = [
        GeneralAmenitiesInline,
        DrinkingAmenitiesInline,
        BathroomAmenitiesInline,
        ViewAmenitiesInline,
        CustomGeneralAmenitiesInline,
        CustomDrinkingAmenitiesInline,
        CustomBathroomAmenitiesInline,
        CustomViewAmenitiesInline,
    ]
