from django.db import models
from .paciente import Paciente

class SigVitales (models.Model):
    id = models.AutoField(primary_key = True)
    idPaciente = models.ForeignKey(Paciente, related_name = 'sigVitales', on_delete = models.CASCADE)
    oximetria = models.CharField('Oximetria', max_length = 30)
    fRespiratiria = models.CharField('FreRespiratoria', max_length = 30)
    fCardiaca = models.CharField('FreCardiaca', max_length = 30)
    temperatura = models.CharField('Temperatura', max_length = 30)
    glicemias = models.CharField('Glicemias', max_length = 30)
    pArterial = models.CharField('PreArterial', max_length = 30)
    fechaHora = models.DateTimeField()
