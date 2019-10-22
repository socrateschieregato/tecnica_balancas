from django.contrib import admin

from .models import (
    Cargo,
    Departamento,
    Desvio,
    Grupo_Empresas,
    Unidade
)

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Grupo_Empresas)
admin.site.register(Unidade)
admin.site.register(Desvio)
