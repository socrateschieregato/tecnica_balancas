from datetime import timezone
from django.db import models
from apps.tabelas.models import Pais, Municipio, Estado, Grupo_Empresas


class Endereco(models.Model):
    tipo = models.CharField(max_length=10)
    tipo_log = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=30)
    cep = models.CharField(max_length=9)
    uf = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    principal = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_log + ' ' + self.endereco + ', ' + self.numero


class Telefone(models.Model):
    tipos = (('1','Fone'), ('2','Cel'), ('3','Outro'),)
    tipo = models.CharField(max_length=10, choices=tipos, default='1')
    ddd = models.CharField('DDD', max_length=2)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return '(' + self.ddd + ') ' + self.numero


class Empresa(models.Model):
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14)
    ie = models.CharField('Inscrição Estadual', max_length=12)
    nome_razao = models.CharField('Nome/Razão', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50)
    telefone = models.ManyToManyField(Telefone)
    email = models.CharField(max_length=50)
    endereco = models.ManyToManyField(Endereco)
    im = models.CharField(max_length=8)
    grupo = models.ForeignKey(Grupo_Empresas, on_delete=models.CASCADE)
    dt_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia




