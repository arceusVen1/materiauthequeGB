from django.conf.urls import url, include
from rest_framework import routers
from .views.materiau import MateriauViewSet
from .views.fournisseur import FournisseurViewSet

router = routers.DefaultRouter()
router.register(r'materiaux', MateriauViewSet)
router.register(r'fournisseurs', FournisseurViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
