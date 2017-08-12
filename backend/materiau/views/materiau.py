from rest_framework import viewsets
from materiau.serializers.materiau import MateriauSerializer
from materiau.models.materiau import Materiau


class MateriauViewSet(viewsets.ModelViewSet):

    queryset = Materiau.objects.all()
    serializer_class = MateriauSerializer

    def perform_create(self, serializer):
        serializer.save()
