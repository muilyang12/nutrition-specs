from django.db import models
from django.db.models import Index


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_key = models.CharField(max_length=100, unique=True)

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
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    serving_size = models.FloatField()
    calory = models.FloatField()
    carbohydrate = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()

    class Meta:
        indexes = [
            Index(fields=["product"]),
        ]

    def __str__(self):
        return f"{self.product.product_name} - {self.calory} kcal"
