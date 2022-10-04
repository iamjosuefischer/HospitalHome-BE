from django.db import models
from .paciente import Paciente


class Signos_vitales(models.Model):
    id_sigvitales = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='sigvitales', on_delete=models.CASCADE)
    oximetria = models.CharField('SugerenciasOximetria', max_length=30)
    frecuenciaRespiratoria = models.CharField('Frecuencia_respiratoria', max_length=30)
    frecuenciaCardiaca = models.CharField('Frecuencia_cardiaca', max_length=30)
    temperatura = models.CharField('Temperatura', max_length=30)
    glicemias = models.CharField('Glicemias', max_length=150)
    presionArterial = models.CharField('Presion_arterial', max_length=30)
    fechaHora = models.DateTimeField()