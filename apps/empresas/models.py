from django.db import models
from apps.tabelas.models import Pais, Municipio, Estado


class Endereco(models.Model):
    tipo = models.CharField(max_length=10)
    tipo_log = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(30)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    pais
    municipio
    principal = models.BooleanField(default=True)


class Telefone(models.Model):
    tipo = models.CharField(max_length=10)
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)


class Empresa(models.Model):
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14)
    ie = models.CharField('Inscrição Estadual', max_length=12)
    nome_razao = models.CharField('Nome/Razão', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50)
    telefone = models.ManyToManyField('Telefone')
    email = models.CharField(max_length=50)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    im = models.CharField(max_length=8)
    grupo
    dt_criacao
    user



