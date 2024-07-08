from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers


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
