from django.contrib import admin

from apps.calibracoes.models import Calibracao, Certificado, Conjunto, Peso
from apps.equipamentos.models import Equipamento, Tipo_equipamento

admin.site.register(Peso)
admin.site.register(Conjunto)
admin.site.register(Certificado)
admin.site.register(Equipamento)
admin.site.register(Tipo_equipamento)
admin.site.register(Calibracao)


class CalibracaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dt_calib', 'equipamento')
    list_filter = ('dt_calib', 'pesos')