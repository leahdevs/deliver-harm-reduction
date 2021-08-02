from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import SupplyCategoryViewSet, SupplyItemViewSet

router = DefaultRouter()
router.register('categories', SupplyCategoryViewSet)
router.register('items', SupplyItemViewSet)

urlpatterns = [
    path("", include(router.urls))
]
