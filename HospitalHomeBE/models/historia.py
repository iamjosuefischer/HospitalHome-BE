from django.db import models
from.paciente import Paciente

class Historia_clinica(models.Model):
    id_histclinica=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente,related_name='histclinica', on_delete=models.CASCADE)
    sugerencias=models.CharField('Sugerencias', max_length=300)
    diagnostico=models.CharField('Diagnostico', max_length=300)
    entorno=models.CharField('Entorno', max_length=300)
    fecha_sugerencia=models.DateField()
    descripcion=models.CharField('Descripcion', max_length=300)