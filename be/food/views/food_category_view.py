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

    @action(detail=False, methods=["get"], url_path="main")
    def get_main_categories(self, request):
        main_categories = self.queryset.filter(parent_category__isnull=True)

        serializer = self.get_serializer(main_categories, many=True)

        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="sub/(?P<main_category_key>[^/.]+)",
    )
    def get_sub_categories(self, request, main_category_key):
        try:
            main_category = self.queryset.get(category_key=main_category_key)
        except models.FoodCategory.DoesNotExist:
            raise ValidationError(code=status.HTTP_404_NOT_FOUND)

        sub_categories = main_category.subCategories.all()

        serializer = self.get_serializer(sub_categories, many=True)

        return Response(serializer.data)
