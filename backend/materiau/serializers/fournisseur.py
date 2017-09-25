from rest_framework import serializers
from materiau.models import Fournisseur


class FournisseurSerializer(serializers.ModelSerializer):

    materiau_set = serializers.StringRelatedField(many=True)


    class Meta:
        model = Fournisseur
        fields = '__all__'
        read_only_fields = ('__all__',)
