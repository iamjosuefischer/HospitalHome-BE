from string import printable
from rest_framework import serializers
from HospitalHomeBE.models.psalud import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'especialidad', 'registro', 'usuario']