from rest_framework import serializers
from .. import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = [
            "id",
            "food_categories",
            "brand",
            "product_name",
            "coupang_url",
        ]


class ProductGetSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = [
            "id",
            "brand_name",
            "product_name",
            "coupang_url",
        ]

    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None
