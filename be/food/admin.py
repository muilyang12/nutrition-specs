from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FoodCategory)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.Nutrition)
admin.site.register(models.MineralVitamin)
