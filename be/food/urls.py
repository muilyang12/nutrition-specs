from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("food-category", views.FoodCategoryViewSet)
router.register("brand", views.BrandViewSet)
router.register("product", views.ProductViewSet)
router.register("nutrition", views.NutritionViewSet)
router.register(
    "product-nutrition", views.ProductNutritionViewSet, basename="product-nutrition"
)

urlpatterns = [
    path("", include(router.urls)),
]
