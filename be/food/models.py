from django.db import models


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_key = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["category_key"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["category_name"], name="unique_category_name"
            ),
            models.UniqueConstraint(
                fields=["category_key"], name="unique_category_key"
            ),
        ]

    def __str__(self):
        return f"{self.category_key} - {self.category_name}"


class Product(models.Model):
    food_categories = models.ManyToManyField(FoodCategory)
    brand_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    coupang_url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["food_category"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["brand_name", "product_name"],
                name="unique_brand_product_name_pair",
            )
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
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        product_name = self.product.product_name if self.product else "None"

        return f"{product_name} - {self.calories} kcal"
