from rest_framework import serializers
from materiau.models.materiau import Materiau


class MateriauSerializer(serializers.ModelSerializer):

    def validate(self, data):
        return data

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Materiau
        fields = ('id',
                  'nom',
                  'sous_famille',
                  'usage',
                  'date_de_creation',
                  'qr_code',
                  'brouillon',
                  'fournisseur',
                  )
        read_only_fields = ('id',
                            'qr_code',
                            )

