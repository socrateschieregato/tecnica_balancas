from django.db import models


class Pais(models.Model):
    cod_ibge = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)


class Municipio(models.Model):
    cod_ibge = models.CharField(max_length=15)
    municipio = models.CharField(max_length=30)


class Estado(models.Model):
    cod_ibge = models.CharField(max_length=15)
    estado = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)


class Grupo_Empresas(models.Model):
    descricao = models.CharField(max_length=20)

