from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("food-category", views.FoodCategoryViewSet)
router.register("brand", views.BrandViewSet)
router.register("product", views.ProductViewSet)
router.register("nutrition", views.NutritionViewSet)
router.register("ingredient", views.IngredientViewSet)
router.register("product-ingredient", views.ProductIngredientViewSet)
router.register("product-detail", views.ProductDatailViewSet, basename="product-detail")
router.register("mineral", views.MineralVitaminViewSet)
router.register("search", views.SearchViewSet, basename="search")

urlpatterns = [
    path("", include(router.urls)),
]
