from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name",
            ),
        ]

    def __str__(self):
        return self.name
