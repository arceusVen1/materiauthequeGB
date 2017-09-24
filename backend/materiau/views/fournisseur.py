from rest_framework import mixins
from rest_framework import viewsets
from materiau.models.fournisseur import Fournisseur
from ..serializers.fournisseur import FournisseurSerializer


class FournisseurViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
        A viewset that provides `retrieve`, and `list` actions.
    """

    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
