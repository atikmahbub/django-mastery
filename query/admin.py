from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "price", "content"]}),
        ("Status", {"fields": ["status"]}),
        ("Locations", {"fields": ["locations"]}),
    ]
    list_display = ("name", "status", "updated_at")
    list_filter = ["status"]
    search_fields = ["price"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(RejectedProduct)
admin.site.register(ProductLocations)
