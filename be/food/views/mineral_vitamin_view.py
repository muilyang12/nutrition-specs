from rest_framework import viewsets

from .. import models, serializers


class MineralVitaminViewSet(viewsets.ModelViewSet):
    queryset = models.MineralVitamin.objects.all()
    serializer_class = serializers.MineralVitaminSerializer
