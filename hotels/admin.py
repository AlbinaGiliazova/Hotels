from django.contrib import admin

from hotels.models import Distance, Hotel, HotelAmenity, HotelPhoto, Rule, VacationType


class HotelAmenityInline(admin.TabularInline):
    model = HotelAmenity
    extra = 1


class RuleInline(admin.TabularInline):
    model = Rule
    extra = 1


class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1


class DistanceInline(admin.TabularInline):
    model = Distance
    extra = 1


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel_type", "category", "country", "city", "address", "vacation_type")
    list_filter = ("hotel_type", "category", "country", "city", "vacation_type")
    search_fields = ("name", "city", "country", "address")
    inlines = [HotelAmenityInline, RuleInline, HotelPhotoInline, DistanceInline]
    fieldsets = (
        (None, {"fields": ("name", "hotel_type", "category", "vacation_type")}),
        ("Локация", {"fields": ("country", "city", "address", "latitude", "longitude")}),
        ("Время заезда и выезда", {"fields": ("check_in_time", "check_out_time")}),
        ("Описание", {"fields": ("description",)}),
    )


@admin.register(VacationType)
class VacationTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "hotel")
    list_filter = ("name", "hotel")
    search_fields = ("name",)
    ordering = ("hotel", "name")


@admin.register(HotelAmenity)
class HotelAmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "amenity_type", "hotel", "icon")
    list_filter = ("amenity_type", "hotel")
    search_fields = ("name",)
    ordering = ("hotel", "name")


@admin.register(Rule)
class HotelRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "hotel", "is_checked")
    list_filter = ("hotel", "is_checked")
    search_fields = ("name",)
    ordering = ("hotel", "name")


@admin.register(HotelPhoto)
class HotelPhotoAdmin(admin.ModelAdmin):
    list_display = ("hotel", "description", "image")
    list_filter = ("hotel",)
    search_fields = ("description",)
    ordering = ("hotel",)
