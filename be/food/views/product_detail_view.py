from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers
from ..pagination import CustomPageNumberPagination


class ProductDatailViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDatailSerializer
    pagination_class = CustomPageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)

        response["Cache-Control"] = "max-age=3600"

        return response

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get("food-category")
        category_key = request.query_params.get("category-key")
        brands = self.request.query_params.getlist("brand")

        if not category_id and not category_key:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)

        if category_id:
            queryset = self.queryset.filter(food_categories=category_id).distinct()

        elif category_key:
            queryset = self.queryset.filter(
                food_categories__category_key=category_key
            ).distinct()

        if brands:
            queryset = queryset.filter(brand__name__in=brands).distinct()

        queryset_with_page = self.paginate_queryset(queryset)

        if queryset_with_page:
            serializer = self.get_serializer(queryset_with_page, many=True)
            response = self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            response = Response(serializer.data)

        response["Cache-Control"] = "max-age=3600"

        return response
