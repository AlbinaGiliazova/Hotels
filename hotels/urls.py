from rest_framework.routers import DefaultRouter

from hotels.views import (
    DistanceViewSet,
    HotelAmenityViewSet,
    HotelPhotoViewSet,
    HotelViewSet,
    RuleViewSet,
    VacationTypeViewSet,
)

router = DefaultRouter()
router.register(r"hotels", HotelViewSet, basename="hotels")
router.register(r"vacation-types", VacationTypeViewSet)
router.register(r"distances", DistanceViewSet)
router.register(r"amenities", HotelAmenityViewSet)
router.register(r"rules", RuleViewSet)
router.register(r"photos", HotelPhotoViewSet)

urlpatterns = router.urls
