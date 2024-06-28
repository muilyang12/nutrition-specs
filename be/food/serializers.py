from rest_framework import serializers
from . import models


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key", "parent_category"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ["id", "food_categories", "name"]


class ProductSerializer(serializers.ModelSerializer):
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


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nutrition
        fields = [
            "id",
            "product",
            "s3_url",
            "data",
        ]
