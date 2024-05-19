from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.FoodCategory.objects.all()
    serializer_class = serializers.FoodCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def list(self, request, *args, **kwargs):
        food_category_id = request.query_params.get("food-category")

        if not food_category_id:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        result = self.queryset.filter(food_category_id=food_category_id)
        serializer = self.get_serializer(result, many=True)

        return Response(serializer.data)


class NutritionViewSet(viewsets.ModelViewSet):
    queryset = models.Nutrition.objects.all()
    serializer_class = serializers.NutritionSerializer

    def list(self, request, *args, **kwargs):
        product_ids = request.query_params.getlist("product")

        if not product_ids:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        result = self.queryset.filter(product__id__in=product_ids)
        serializer = self.get_serializer(result, many=True)

        return Response(serializer.data)
