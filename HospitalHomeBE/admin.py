from django.contrib import admin
from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.enfermero import Enfermero
from .models.rol import Rol

# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Familiar)
admin.site.register(Enfermero)
admin.site.register(Medico)
admin.site.register(Paciente)