from rest_framework import mixins
from rest_framework import viewsets
from materiau.models import Famille, SousFamille
from ..serializers import FamilleSerializer, SousFamilleSerializer


class FamilleViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
        A viewset that provides `retrieve`, and `list` actions.
    """

    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer

    # url de recherche utilise la référence
    lookup_field = 'reference'


class SousFamilleViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
        A viewset that provides `retrieve`, and `list` actions.
    """

    queryset = SousFamille.objects.all()
    serializer_class = SousFamilleSerializer