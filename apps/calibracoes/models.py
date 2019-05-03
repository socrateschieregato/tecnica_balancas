from django.db import models
from apps.empresas.models import Empresa
from apps.tabelas.models import Unidade, Usuario


class Tipo_equipamento(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao

class Conjunto(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao

class Desvio(models.Model):
    valor = models.DecimalField()
    un = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.valor + ' ' + self.un

class Certificado(models.Model):
    numero = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero + ' ' + str(self.data)

class Equipamento(models.Model):
    status_choices = ((1,'Ativo'), (1,'Inativo'),(1,'Pendente'))
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    num_registro = models.CharField(max_length=20)
    tipo = models.ForeignKey(Tipo_equipamento, on_delete=models.CASCADE)
    fabricante = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    escala_ini = models.DecimalField()
    escala_fim = models.DecimalField()
    num_serie = models.CharField(max_length=20)
    tag = models.CharField(max_length=10)
    status = models.CharField(choices=status_choices, default=1)
    desvio = models.ForeignKey(Desvio, on_delete=models.PROTECT)
    n_estrategia = models.IntegerField()
    departamento = models.CharField(max_length=20)
    resolucao_1 = models.DecimalField()
    resolucao_2 = models.DecimalField()
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, models.PROTECT)

    def __str__(self):
        return self.tipo.descricao + ' - ' + self.num_registro


class Calibracao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    periodicidade = models.IntegerField()
    dt_calib = models.DateField(auto_now=True)
    dt_calib_next = models.DateField()
    ajuste = models.CharField(max_length=30)
    obs = models.CharField(max_length=50)
    certificado = models.ForeignKey(Certificado, on_delete=models.PROTECT)
    pesos = models.ForeignKey()
    umidade = models.DecimalField()
    pressao = models.DecimalField()
    temperatura = models.DecimalField()
    desvio_adotado = models.CharField(max_length=20)
    responsavel = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    tipo_calibracao = models.CharField()
    num_os = models.IntegerField()
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
    material = models.CharField()
    incerteza_mg = models.FloatField()
    certificado = models.CharField()
    fator_abrangencia = models.FloatField()
    status = models.BooleanField(default=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, models.PROTECT)

    def __str__(self):
        return self.conjunto.descricao + ' - ' + str(self.massa_nominal_g)\
               + ' ' + self.unidade.sigla