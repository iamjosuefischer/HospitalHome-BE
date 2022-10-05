from django.db import models
from .usuario import Usuario


class Personal_salud(models.Model):
    id= models.BigAutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name='Psalud', on_delete=models.CASCADE)
    rol = models.CharField('Rol', max_length=30)
    especialidad = models.CharField('Especialidad', max_length=30)