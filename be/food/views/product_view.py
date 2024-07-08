from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers
from ..pagination import CustomPageNumberPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return serializers.ProductGetSerializer

        return serializers.ProductSerializer

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
