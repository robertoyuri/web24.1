from django.contrib import admin

from .models import Paciente, Medico, Consulta
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)