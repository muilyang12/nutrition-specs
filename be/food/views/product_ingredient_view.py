from rest_framework import viewsets

from .. import models, serializers


class ProductIngredientViewSet(viewsets.ModelViewSet):
    queryset = models.ProductIngredient.objects.all()
    serializer_class = serializers.ProductIngredientSerializer
