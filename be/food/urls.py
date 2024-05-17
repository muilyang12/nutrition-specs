from django.urls import path
from . import views

urlpatterns = [
    path("food-category/", views.food_category, name="food_category"),
    path("product/", views.product, name="product"),
    path("nutrition/", views.nutrition, name="nutrition"),
]
