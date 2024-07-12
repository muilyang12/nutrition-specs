from django.db import models


class MineralVitamin(models.Model):
    name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name