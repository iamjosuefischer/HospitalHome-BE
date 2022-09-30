from rest_framework import serializers
from HospitalHomeBE.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        models= Familiar
        fields=['parentezco', 'usuario']