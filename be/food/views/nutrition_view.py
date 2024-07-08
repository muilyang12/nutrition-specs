from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .. import models, serializers


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
