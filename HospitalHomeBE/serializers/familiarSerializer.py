from string import printable
from rest_framework import serializers
from HospitalHomeBE.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:       
        model= Familiar
        fields=('parentezco', 'usuario')