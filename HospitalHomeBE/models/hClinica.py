from django.db import models
from .paciente import Paciente

class HisClinica (models.Model):
    id = models.AutoField(primary_key = True)
    idPaciente = models.ForeignKey(Paciente, related_name ='hClinica', on_delete = models.CASCADE)
    sugCuidado = models.CharField('SugCuidado', max_length = 500)
    diagnostico = models.CharField('Diagnostico', max_length = 100)
    entorno = models.CharField('Entorno', max_length = 100)
    fSugerencia = models.DateField()
    descripcion = models.CharField('Descripcion', max_length = 800)