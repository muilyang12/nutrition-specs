from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.FoodCategory.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return serializers.FoodCategoryGetSerializer

        return serializers.FoodCategorySerializer

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
