from django.db import models
from apps.empresas.models import Empresa
from apps.tabelas.models import Unidade, Usuario
from apps.equipamentos.models import Equipamento


class Conjunto(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Certificado(models.Model):
    numero = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero + ' ' + str(self.data)


class Calibracao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    periodicidade = models.IntegerField()
    dt_calib = models.DateField('Data Calibração', auto_now=True)
    dt_calib_next = models.DateField('Próxima Calibração')
    ajuste = models.CharField(max_length=30)
    obs = models.CharField(max_length=50)
    certificado = models.ForeignKey(Certificado, on_delete=models.PROTECT)
    pesos = models.ManyToManyField('Peso')
    umidade = models.DecimalField(decimal_places=2, max_digits=14)
    pressao = models.DecimalField(decimal_places=2, max_digits=14)
    temperatura = models.DecimalField(decimal_places=2, max_digits=14)
    desvio_adotado = models.CharField('Desvio Adotado', max_length=20)
    responsavel = models.ForeignKey(Usuario, on_delete=models.PROTECT,
                                    related_name='Calibracao_usuario')
    tipo_calibracao = models.CharField(max_length=10)
    num_os = models.IntegerField('Número OS')
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, models.PROTECT)

    def __str__(self):
        return self.equipamento.empresa.nome_fantasia + ' - '\
               + self.equipamento.tipo.descricao + ' ' + str(self.dt_calib)


class Peso(models.Model):
    massa_nominal_g = models.FloatField()
    marcacao = models.CharField(max_length=20)
    classe = models.CharField(max_length=20)
    identificacao = models.CharField(max_length=20)
    conjunto = models.ForeignKey(Conjunto, on_delete=models.PROTECT)
    massa_conv_mg_1 = models.FloatField()
    erro_1 = models.FloatField()
    massa_conv_mg_2 = models.FloatField()
    erro_2 = models.FloatField()
    dt_calibracao = models.DateField()
    validade = models.DateField()
    material = models.CharField(max_length=20)
    incerteza_mg = models.FloatField()
    certificado = models.CharField(max_length=20)
    fator_abrangencia = models.FloatField()
    status = models.BooleanField(default=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, models.PROTECT)

    def __str__(self):
        return self.conjunto.descricao + ' - ' + str(self.massa_nominal_g)\
               + ' ' + self.unidade.sigla