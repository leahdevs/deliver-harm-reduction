from rest_framework import viewsets

from .models import SupplyCategory, SupplyItem
from .serializers import SupplyCategorySerializer, SupplyItemSerializer


class SupplyCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SupplyCategorySerializer
    queryset = SupplyCategory.objects.all()


class SupplyItemViewSet(viewsets.ModelViewSet):
    serializer_class = SupplyItemSerializer
    queryset = SupplyItem.objects.all()
