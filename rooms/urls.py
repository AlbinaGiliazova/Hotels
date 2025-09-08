from rest_framework.routers import DefaultRouter

from rooms.views import AmenityViewSet, RoomPhotoViewSet, RoomViewSet, RuleViewSet

router = DefaultRouter()
router.register("rooms", RoomViewSet)
router.register("amenities", AmenityViewSet)
router.register("rules", RuleViewSet)
router.register("photos", RoomPhotoViewSet)

urlpatterns = router.urls
