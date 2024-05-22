from rest_framework import serializers
from . import models


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "food_category", "brand_name", "product_name"]


class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nutrition
        fields = [
            "id",
            "product",
            "serving_size",
            "calory",
            "carbohydrate",
            "protein",
            "fat",
        ]
