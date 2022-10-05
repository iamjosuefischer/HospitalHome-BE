from HospitalHomeBE.models.historia import Historia_clinica
from rest_framework import serializers

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historia_clinica
        fields=('id_paciente','sugerencias','diagnostico','entorno','fecha_sugerencia''descripcion')