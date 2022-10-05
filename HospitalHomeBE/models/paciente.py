from django.db import models
from .user import User
from .pSalud import PersonalSalud

class Paciente(models.Model):
    id = models.AutoField(primary_key = True)
    perSalud = models.ForeignKey(PersonalSalud, related_name = 'paciente', on_delete = models.CASCADE)
    iduser = models.ForeignKey(User, related_name = 'paciente', on_delete = models.CASCADE)
    direccion = models.CharField('Direccion', max_length = 30)
    ciudad = models.CharField('Ciudad',max_length = 30)
    fNacimiento = models.DateField('FechaNacimiento')