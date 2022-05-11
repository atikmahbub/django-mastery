from dataclasses import field
from rest_framework import serializers
from .models import Product, RejectedProduct


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "content",
            "price",
            "discount_price",
            "my_discount",
            "created_at",
            "updated_at",
            "status",
        )

    def get_my_discount(self, obj):
        return obj.get_discount()


class RejectedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectedProduct
        fields = (
            "id",
            "name",
            "rejected_date",
            "status",
        )
