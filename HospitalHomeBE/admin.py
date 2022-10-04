from django.contrib import admin
from .models.usuario import Usuario
from .models.psalud import Personal_salud
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.sigvitales import Signos_vitales
from .models.historia import Historia_clinica

admin.site.register(Usuario)
admin.site.register(Personal_salud)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Signos_vitales)
admin.site.register(Historia_clinica)