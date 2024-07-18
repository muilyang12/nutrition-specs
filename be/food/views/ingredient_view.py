from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def list(self, request, *args, **kwargs):
        ingredient_ids = request.query_params.getlist("ingredient")

        if not ingredient_ids:
            return ValidationError(code=status.HTTP_400_BAD_REQUEST)

        result = self.queryset.filter(id__in=ingredient_ids)
        serializer = self.get_serializer(result, many=True)

        response = Response(serializer.data)

        response["Cache-Control"] = "max-age=86400"

        return response
