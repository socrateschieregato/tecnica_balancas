from django.contrib import admin

from .models import (
    Departamento,
    Desvio,
    Unidade
)

admin.site.register(Departamento)
admin.site.register(Unidade)
admin.site.register(Desvio)
