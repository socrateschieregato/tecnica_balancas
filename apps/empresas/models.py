from datetime import timezone
from django.db import models
from apps.tabelas.models import Pais, Municipio, Estado, Grupo_Empresas


class Empresa(models.Model):
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14)
    ie = models.CharField('Inscrição Estadual', max_length=12)
    nome_razao = models.CharField('Nome/Razão', max_length=100)
    nome_fantasia = models.CharField('Nome Fantasia', max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50)
    im = models.CharField(max_length=8, null=True, blank=True)
    grupo = models.ForeignKey(Grupo_Empresas, on_delete=models.CASCADE, null=True, blank=True)
    dt_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia

class Endereco(models.Model):
    tipos = (('1', 'Rua'), ('2', 'Av'), ('3', 'Rod'),('4', 'Outro'),)
    tipo_log = models.CharField(max_length=10, choices=tipos, default='1')
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=30, null=True, blank=True)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    cep = models.CharField(max_length=9)
    uf = models.ForeignKey(Estado, on_delete=models.PROTECT)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_log + ' ' + self.endereco + ', ' + str(self.numero)


class Telefone(models.Model):
    tipos = (('1','Fone'), ('2','Cel'), ('3','Outro'),)
    tipo = models.CharField(max_length=10, choices=tipos, default='1')
    ddd = models.CharField('DDD', max_length=2, null=True, blank=True)
    num_tel = models.CharField(max_length=10, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return '(' + self.ddd + ') ' + self.numero





