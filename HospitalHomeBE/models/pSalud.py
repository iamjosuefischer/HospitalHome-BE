from django.db import models
from .user import User

class PersonalSalud (models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    iduser = models.ForeignKey(User, related_name = 'pSalud', on_delete = models.CASCADE)
    rol = models.CharField('Rol', max_length = 30)
    especialidad = models.CharField('Especialidad', max_length = 30)
