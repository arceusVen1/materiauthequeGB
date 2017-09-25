from rest_framework import mixins
from rest_framework import viewsets
from materiau.models import Famille
from ..serializers import FamilleSerializer


class FamilleViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
        A viewset that provides `retrieve`, and `list` actions.
    """

    queryset = Famille.objects.all()
    serializer_class = FamilleSerializer
