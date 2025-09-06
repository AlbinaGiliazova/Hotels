"""Маршруты приложения."""

from rest_framework.routers import DefaultRouter

from .views import MealTypeViewSet

router = DefaultRouter()
router.register(r"meal_type", MealTypeViewSet, basename="meal_type")

urlpatterns = router.urls
