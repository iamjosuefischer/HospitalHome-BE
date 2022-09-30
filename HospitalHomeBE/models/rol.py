from django.db import models

class Rol(models.Model):
    class TipoUsuario(models.TextChoices):
        PACIENTE = 'Paciente'
        FAMILIAR = 'Familiar'
        AUXILIAR = 'Auxiliar'
        MEDICO = 'Medico'
        ENFERMERO = 'Enfermero'
    
    tipo_usuario = models.CharField(primary_key=True, max_length=9, choices=TipoUsuario.choices)
    permisos = models.IntegerField(default=0)