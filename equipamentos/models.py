from django.contrib.auth.models import User
from django.db import models

from empresas.models import Empresa
from tabelas.models import Desvio


class Tipo_equipamento(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao


class Equipamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    num_registro = models.CharField('Número de Registro', max_length=20, null=True, blank=True)
    tipo = models.ForeignKey(Tipo_equipamento, on_delete=models.CASCADE, null=True, blank=True)
    fabricante = models.CharField(max_length=20, null=True, blank=True)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    escala = models.CharField(max_length=30, null=True, blank=True)
    num_serie = models.CharField('Número de Série', max_length=20, null=True, blank=True)
    tag = models.CharField(max_length=10, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    desvio = models.ForeignKey(Desvio, on_delete=models.PROTECT, null=True, blank=True)
    n_estrategia = models.IntegerField(null=True, blank=True)
    departamento = models.CharField('Departamento', max_length=20, null=True, blank=True)
    resolucao_1 = models.DecimalField(
        'Resolução 1',
        decimal_places=2,
        max_digits=14,
        null=True,
        blank=True
    )
    resolucao_2 = models.DecimalField(
        'Resolução 2',
        decimal_places=2,
        max_digits=14,
        null=True,
        blank=True
    )
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, models.PROTECT)
    pontos_calib = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.tipo.descricao + ' - ' + self.num_registro
