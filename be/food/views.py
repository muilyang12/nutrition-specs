from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from . import models, serializers


class FoodCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.FoodCategory.objects.all()
    serializer_class = serializers.FoodCategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("food-category")
        category_key = request.query_params.get("category-key")

        if not category_id and not category_key:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        data = None

        if category_id:
            result = self.queryset.filter(food_category_id=category_id)
            serializer = self.get_serializer(result, many=True)
            data = serializer.data

        elif category_key:
            result = self.queryset.select_related("food_category").filter(
                food_category__category_key=category_key
            )
            serializer = self.get_serializer(result, many=True)
            data = serializer.data

        return Response(data)


class NutritionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Nutrition.objects.all()
    serializer_class = serializers.NutritionSerializer

    def list(self, request, *args, **kwargs):
        product_ids = request.query_params.getlist("product")

        if not product_ids:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        result = self.queryset.filter(product__id__in=product_ids)
        serializer = self.get_serializer(result, many=True)

        return Response(serializer.data)
