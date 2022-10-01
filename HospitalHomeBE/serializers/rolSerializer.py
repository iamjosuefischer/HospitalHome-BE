from rest_framework import serializers
from HospitalHomeBE.models.rol import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields=['tipo_usuario','permisos']