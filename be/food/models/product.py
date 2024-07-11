from django.db import models

from . import FoodCategory, Brand


class Product(models.Model):
    food_categories = models.ManyToManyField(FoodCategory)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    product_name = models.CharField(max_length=100)
    coupang_url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["brand", "product_name"],
                name="unique_brand_product_name_pair",
            )
        ]

    def __str__(self):
        brand_name = self.brand.name if self.brand else "None"

        return f"{brand_name} - {self.product_name}"
