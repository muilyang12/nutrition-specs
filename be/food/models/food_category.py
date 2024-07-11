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
