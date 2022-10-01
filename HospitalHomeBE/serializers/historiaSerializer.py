from rest_framework import serializers
from HospitalHomeBE.models.historia import Historia


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historia
        fields=['paciente', 'oximetria', 'f_respiratoria', 'f_cardiaca', 'temperatura', 'presion_arterial', 'glicemias', 'diagnostico' ,'cuidados']