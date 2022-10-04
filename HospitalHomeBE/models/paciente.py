from django.db import models
from .usuario import Usuario
from .psalud import Personal_salud


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_psalud = models.ForeignKey(Personal_salud, related_name='Paciente', on_delete=models.CASCADE)
    username = models.ForeignKey(Usuario, related_name='Paciente', on_delete=models.CASCADE)
    direccion = models.CharField(('Direccion'), max_length=50)
    ciudad = models.CharField('Ciudad', max_length=30)
    fecha_nacimiento = models.DateField()