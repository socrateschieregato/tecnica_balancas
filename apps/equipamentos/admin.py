from django.contrib import admin

from apps.equipamentos.models import Equipamento, Tipo_equipamento


admin.site.register(Equipamento)
admin.site.register(Tipo_equipamento)