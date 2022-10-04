from HospitalHomeBE.models.familiar import Familiar
from rest_framework import serializers

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields=('username','parentesco','correo')