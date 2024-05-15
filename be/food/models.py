from django.db import models


# Create your models here.
class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    food_category = models.ForeignKey(
        FoodCategory, on_delete=models.SET_NULL, null=True
    )
    brand_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand_name} - {self.product_name}"


class Nutrition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    serving_size = models.FloatField()
    calory = models.FloatField()
    carbohydrate = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return f"{self.product.product_name} - {self.calory} kcal"
