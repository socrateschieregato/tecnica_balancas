from django.contrib import admin

from .models import Empresa, Endereco, Telefone

admin.site.register(Endereco)
admin.site.register(Empresa)
admin.site.register(Telefone)
