from django.contrib import admin

from .models import SupplyCategory, SupplyItem

admin.site.register(SupplyCategory)
admin.site.register(SupplyItem)
