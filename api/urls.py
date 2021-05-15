from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]