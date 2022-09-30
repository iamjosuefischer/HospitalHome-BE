from rest_framework import serializers
from HospitalHomeBE.models.enfermero import Enfermero

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['usuario', 'area', 'auxiliar']