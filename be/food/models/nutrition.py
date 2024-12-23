from django.db import models

from . import Product


class Nutrition(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, null=True, related_name="nutritions"
    )
    s3_key = models.CharField(max_length=300, null=True, blank=True)
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
