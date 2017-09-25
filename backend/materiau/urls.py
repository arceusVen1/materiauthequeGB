from django.conf.urls import url, include
from rest_framework import routers
from .views.materiau import MateriauViewSet
from .views.fournisseur import FournisseurViewSet
from .views.famille import FamilleViewSet, SousFamilleViewSet

router = routers.DefaultRouter()
router.register(r'materiaux', MateriauViewSet)
router.register(r'fournisseurs', FournisseurViewSet)
router.register(r'familles', FamilleViewSet)
router.register(r'sous-familles', SousFamilleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
