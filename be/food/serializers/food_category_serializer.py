from rest_framework import serializers
from .. import models


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key", "parent_category"]


class FoodCategoryGetSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.FoodCategory
        fields = ["id", "category_name", "category_key", "parent_category"]

    def get_category_name(self, obj):
        if obj.parent_category:
            return f"{obj.parent_category.category_name} - {obj.category_name}"

        else:
            return obj.category_name
