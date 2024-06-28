from django.db import models


class FoodCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_key = models.CharField(max_length=100)
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subCategories",
    )

    class Meta:
        indexes = [
            models.Index(fields=["category_key"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["category_name", "category_key"],
                name="unique_key_name_pair",
            ),
        ]

    def __str__(self):
        return f"{self.category_key} - {self.category_name}"


class Brand(models.Model):
    food_categories = models.ManyToManyField(FoodCategory)
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_brand_name"),
        ]

    def __str__(self):
        return f"{self.name}"


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


class Nutrition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    s3_url = models.CharField(max_length=300, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        brand_name = (
            self.product.brand.name if self.product and self.product.brand else "None"
        )
        product_name = self.product.product_name if self.product else "None"

        return f"{brand_name} - {product_name}"
