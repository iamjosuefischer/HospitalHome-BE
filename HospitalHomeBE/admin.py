from django.contrib import admin
from .models.user import User
from .models.sigVitales import SigVitales
from .models.familiar import Familiar
from .models.hClinica import HisClinica
from .models.paciente import Paciente
from .models.pSalud import PersonalSalud
from .models.sigVitales import SigVitales
# Register your models here.
admin.site.register(User)
admin.site.register(Familiar)
admin.site.register(HisClinica)
admin.site.register(Paciente)
admin.site.register(PersonalSalud)
admin.site.register(SigVitales)