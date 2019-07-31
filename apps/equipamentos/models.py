from django.db import models
from apps.tabelas.models import Usuario, Desvio
from apps.empresas.models import Empresa


class Tipo_equipamento(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao


class Equipamento(models.Model):
    status_choices = ((1,'Ativo'), (1,'Inativo'),(1,'Pendente'))
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    num_registro = models.CharField('Número de Registro' ,max_length=20)
    tipo = models.ForeignKey(Tipo_equipamento, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    escala_ini = models.DecimalField('Escala Inicial', decimal_places=2, max_digits=14)
    escala_fim = models.DecimalField('Escala Final',decimal_places=2, max_digits=14)
    num_serie = models.CharField('Número de Série', max_length=20)
    tag = models.CharField(max_length=10)
    status = models.CharField('Status', choices=status_choices, default=1, max_length=10)
    desvio = models.ForeignKey(Desvio, on_delete=models.PROTECT)
    n_estrategia = models.IntegerField()
    departamento = models.CharField('Departamento', max_length=20)
    resolucao_1 = models.DecimalField('Resolução 1', decimal_places=2, max_digits=14)
    resolucao_2 = models.DecimalField('Resolução 2',decimal_places=2, max_digits=14)
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, models.PROTECT)

    def __str__(self):
        return self.tipo.descricao + ' - ' + self.num_registro
