from rest_framework import serializers
from materiau.models import Famille


class FamilleSerializer(serializers.ModelSerializer):

    sousfamille_set = serializers.StringRelatedField(many=True)


    class Meta:
        model = Famille
        fields = '__all__'
        read_only_fields = ('__all__',)
