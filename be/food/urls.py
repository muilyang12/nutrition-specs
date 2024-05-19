from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("food-category", views.FoodCategoryViewSet)
router.register("product", views.ProductViewSet)
router.register("nutrition", views.NutritionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
