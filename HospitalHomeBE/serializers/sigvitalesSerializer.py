from pyexpat import model
from HospitalHomeBE.models.sigVitales import SigVitales
from rest_framework import serializers

class SigVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SigVitales
        fields = ('idPaciente', 'oximetria', 'fRespiratiria', 'fCardiaca', 'temperatura', 'glicemias', 'pArterial', 'fechaHora')