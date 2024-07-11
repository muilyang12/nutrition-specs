from rest_framework import serializers

from .. import models


class ProductIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductIngredient
        fields = [
            "id",
            "product",
            "s3_key",
            "ingredients",
        ]
