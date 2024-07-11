from django.db import models

from . import FoodCategory


class Brand(models.Model):
    food_categories = models.ManyToManyField(FoodCategory)
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_brand_name"),
        ]

    def __str__(self):
        return f"{self.name}"
