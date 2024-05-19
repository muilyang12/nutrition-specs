from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . import models, serializers


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.FoodCategory.objects.all()
    serializer_class = serializers.FoodCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class NutritionViewSet(viewsets.ModelViewSet):
    queryset = models.Nutrition.objects.all()
    serializer_class = serializers.NutritionSerializer
