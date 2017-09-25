from rest_framework import serializers
from materiau.models import Famille
from materiau.models import SousFamille


class SousFamilleSerializer(serializers.ModelSerializer):

    materiau_set = serializers.StringRelatedField(many=True)

    # on récupère plutot la référence plutot que l'id de la famille pour construire l'url
    famille = serializers.SlugRelatedField(many=False, read_only=True, slug_field='reference')

    class Meta:
        model = SousFamille
        fields = ('materiau_set',
                  'matiere',
                  'numero_de_reference',
                  'famille',
                  'reference',
                  'nombre_de_materiaux',)

        read_only_fields = ('__all__',)


class FamilleSerializer(serializers.ModelSerializer):

    sousfamille_set = SousFamilleSerializer(many=True, read_only=True)

    class Meta:
        model = Famille
        fields = '__all__'
        read_only_fields = ('__all__',)



