from django.contrib.auth.models import User
from django.db import models

from calibracoes.enums import StatusClass
from equipamentos.models import Equipamento
from tabelas.enums import WeightClass, WeightMaterials
from tabelas.models import Unidade, Conjunto


class Certificado(models.Model):
    numero = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero + ' ' + (self.data).strftime("%d/%m/%Y")


class Calibracao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    periodicidade = models.IntegerField()
    dt_calib = models.DateField('Data Calibração', auto_now=True)
    dt_calib_next = models.DateField('Próxima Calibração')
    ajuste = models.CharField(max_length=30, null=True, blank=True)
    obs = models.CharField(max_length=50, null=True, blank=True)
    certificado = models.ForeignKey(Certificado, on_delete=models.PROTECT)
    pesos = models.ManyToManyField('Peso')
    umidade = models.DecimalField(decimal_places=2, max_digits=14, null=True, blank=True)
    pressao = models.DecimalField(decimal_places=2, max_digits=14, null=True, blank=True)
    temperatura = models.DecimalField(decimal_places=2, max_digits=14, null=True, blank=True)
    desvio_adotado = models.CharField('Desvio Adotado', max_length=20, null=True, blank=True)
    responsavel = models.ForeignKey(
        User, on_delete=models.PROTECT,
        related_name='Calibracao_usuario',
    )
    tipo_calibracao = models.CharField(max_length=10, null=True, blank=True)
    num_os = models.IntegerField('Número OS', null=True, blank=True)
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, models.PROTECT)
    status = models.CharField(max_length=20, choices=StatusClass.choices(), null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Calibracoes'

    def __str__(self):
        return f'{self.equipamento.empresa.nome_fantasia} {self.equipamento.tipo.descricao} {str(self.dt_calib)}'  # noqa


class Peso(models.Model):
    massa_nominal_g = models.FloatField()
    marcacao = models.CharField(max_length=20)
    classe = models.CharField(max_length=20, choices=WeightClass.choices(), null=True, blank=True)
    identificacao = models.CharField(max_length=20)
    conjunto = models.ForeignKey(Conjunto, on_delete=models.PROTECT)
    massa_conv_mg_1 = models.FloatField()
    erro_1 = models.FloatField()
    massa_conv_mg_2 = models.FloatField()
    erro_2 = models.FloatField()
    dt_calibracao = models.DateField()
    validade = models.DateField()
    material = models.CharField(max_length=20, choices=WeightMaterials.choices())
    incerteza_mg = models.FloatField()
    certificado = models.CharField(max_length=20)
    fator_abrangencia = models.FloatField()
    ativo = models.BooleanField(default=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, models.PROTECT)

    def __str__(self):
        return f'{self.conjunto.descricao} - {str(self.massa_nominal_g)} {self.unidade.sigla}'  # noqa
