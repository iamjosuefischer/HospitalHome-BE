from HospitalHomeBE.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=('id_psalud','username','direccion','ciudad','fecha_nacimiento')