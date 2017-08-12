from rest_framework import mixins
from rest_framework import viewsets
from materiau.models.fournisseur import Fournisseur
from ..serializers.fournisseur import FournisseurSerializer


class FournisseurViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):

    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)