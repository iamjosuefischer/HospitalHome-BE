from django.db import models
from .user import User
from .paciente import Paciente

class Familiar(models.Model):
    id = models.AutoField(primary_key = True)
    iduser = models.ForeignKey(User, related_name = 'familiar', on_delete = models.CASCADE)
    idPaciente = models.ForeignKey(Paciente, related_name = 'familiar', on_delete = models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length =40)
    correo = models.EmailField('correo', max_length= 100)