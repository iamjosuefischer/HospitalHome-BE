from rest_framework import serializers
from HospitalHomeBE.models.rol import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        models=Rol
        fields=['tipo_usuario','permisos']