from django.db import models
from django.db.models import Index


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_key = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return f"{self.category_key} - {self.category_name}"


class Product(models.Model):
    food_category = models.ForeignKey(
        FoodCategory, on_delete=models.SET_NULL, null=True
    )
    brand_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            Index(fields=["food_category"]),
        ]

    def __str__(self):
        return f"{self.brand_name} - {self.product_name}"


class Nutrition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    serving_size = models.FloatField(null=True)
    serving_unit = models.CharField(max_length=10, null=True)
    calories = models.FloatField(null=True)
    total_carbohydrate = models.FloatField(null=True)
    dietary_fiber = models.FloatField(null=True)
    sugars = models.FloatField(null=True)
    total_fat = models.FloatField(null=True)
    saturated_fat = models.FloatField(null=True)
    trans_fat = models.FloatField(null=True)
    cholesterol = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    sodium = models.FloatField(null=True)
    calcium = models.FloatField(null=True)

    class Meta:
        indexes = [
            Index(fields=["product"]),
        ]

    def __str__(self):
        return f"{self.product.product_name} - {self.calory} kcal"
