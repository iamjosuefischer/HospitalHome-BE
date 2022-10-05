from pyexpat import model
from HospitalHomeBE.models.hClinica import HisClinica
from rest_framework import serializers

class HisClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HisClinica
        fields = ('idPaciente', 'sugCuidado', 'diagnostico', 'entorno', 'fSugerencia', 'descripcion')