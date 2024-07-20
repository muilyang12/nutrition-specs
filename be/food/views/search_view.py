from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError


class SearchViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def retrieve(self, request):
        query = request.query_params.get("query")

        if not query:
            raise ValidationError(code=status.HTTP_400_BAD_REQUEST)
