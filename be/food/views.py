from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from . import models, serializers
from .pagination import CustomPageNumberPagination


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.FoodCategory.objects.all()
    serializer_class = serializers.FoodCategorySerializer

    @action(
        detail=False, methods=["get"], url_path="category-key/(?P<category_key>[^/.]+)"
    )
    def get_by_category_key(self, request, category_key=None):
        try:
            food_category = self.queryset.get(category_key=category_key)
        except models.FoodCategory.DoesNotExist:
            raise ValidationError(code=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(food_category)

        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("food-category")
        category_key = request.query_params.get("category-key")

        if not category_id and not category_key:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        if category_id:
            result = self.queryset.filter(food_categories=category_id).distinct()

        elif category_key:
            result = self.queryset.filter(
                food_categories__category_key=category_key
            ).distinct()

        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = CustomPageNumberPagination

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("food-category")
        category_key = request.query_params.get("category-key")

        if not category_id and not category_key:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        if category_id:
            result = self.queryset.filter(food_categories=category_id).distinct()

        elif category_key:
            result = self.queryset.filter(
                food_categories__category_key=category_key
            ).distinct()

        result_with_page = self.paginate_queryset(result)
        if result_with_page:
            serializer = self.get_serializer(result_with_page, many=True)
            return self.get_paginated_response(serializer.data)

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


class ProductNutritionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ProductNutritionSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = models.Product.objects.all()
        category_id = self.request.query_params.get("food-category")
        category_key = self.request.query_params.get("category-key")
        brands = self.request.query_params.getlist("brand")

        if category_id:
            queryset = queryset.filter(food_categories=category_id).distinct()

        elif category_key:
            queryset = queryset.filter(
                food_categories__category_key=category_key
            ).distinct()

        if brands:
            queryset = queryset.filter(brand__name__in=brands).distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("food-category")
        category_key = request.query_params.get("category-key")

        if not category_id and not category_key:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()
        queryset_with_page = self.paginate_queryset(queryset)

        if queryset_with_page:
            serializer = self.get_serializer(queryset_with_page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
