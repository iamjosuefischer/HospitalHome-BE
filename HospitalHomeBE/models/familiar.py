from django.db import models
from .usuario import Usuario   
from .paciente import Paciente


class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length=30)
    correo = models.EmailField('Correo', max_length=80)