from rest_framework import serializers

from .. import models


class MineralVitaminSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.MineralVitamin
        fields = ["id", "name", "description"]
