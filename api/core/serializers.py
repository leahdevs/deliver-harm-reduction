from rest_framework import serializers

from .models import SupplyCategory, SupplyItem


class SupplyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyCategory
        fields = ('id', 'name')


class SupplyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyItem
        fields = ('id', 'name', 'picture', 'description')
