from rest_framework import serializers
from .models import Product


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
        )

    def get_my_discount(self, obj):
        return obj.get_discount()
