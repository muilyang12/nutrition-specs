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
    serving_size = models.FloatField(null=True, blank=True)
    serving_unit = models.CharField(max_length=10, null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)
    total_carbohydrate = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    sugar_alcohols = models.FloatField(null=True, blank=True)
    dietary_fiber = models.FloatField(null=True, blank=True)
    allulose = models.FloatField(null=True, blank=True)
    total_fat = models.FloatField(null=True, blank=True)
    saturated_fat = models.FloatField(null=True, blank=True)
    trans_fat = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)

    class Meta:
        indexes = [
            Index(fields=["product"]),
        ]

    def __str__(self):
        return f"{self.product.product_name} - {self.calory} kcal"
