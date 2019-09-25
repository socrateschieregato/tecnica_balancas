from django.contrib import admin

from .models import (
    Cargo,
    Departamento,
    Desvio,
    Estado,
    Grupo_Empresas,
    Municipio,
    Pais,
    Unidade,
    Usuario
)

admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Grupo_Empresas)
admin.site.register(Municipio)
admin.site.register(Pais)
admin.site.register(Usuario)
admin.site.register(Unidade)
admin.site.register(Estado)
admin.site.register(Desvio)
