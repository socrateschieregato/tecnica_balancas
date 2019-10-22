from django.contrib import admin

from calibracoes.models import (
    Calibracao,
    Certificado,
    Conjunto,
    Peso
)

admin.site.register(Peso)
admin.site.register(Conjunto)
admin.site.register(Certificado)
admin.site.register(Calibracao)


class CalibracaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dt_calib', 'equipamento')
    list_filter = ('dt_calib', 'pesos')
