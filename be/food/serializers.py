from rest_framework import serializers
from . import models


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "food_categories", "brand", "product_name", "coupang_url"]


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nutrition
        fields = [
            "id",
            "product",
            "s3_url",
            "data",
        ]
