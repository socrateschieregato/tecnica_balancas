from django.contrib.auth.models import User
from django.db import models


class Departamento(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Cargo(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Usuario(models.Model):
    status_choices = ((1, 'Ativo'), (1, 'Inativo'))
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    cpf = models.CharField('CPF', max_length=11)
    dt_nasc = models.DateField()
    dt_desligamento = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    foto = models.ImageField(
        width_field=50,
        height_field=50,
        null=True,
        blank=True
    )
    smtp = models.CharField(max_length=30, null=True, blank=True)
    porta = models.IntegerField(null=True, blank=True)
    ssl = models.BooleanField(null=True, blank=True)
    status = models.CharField(choices=status_choices, default=1, max_length=10)

    def __str__(self):
        return self.user.username


class Pais(models.Model):
    cod_ibge = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.pais


class Estado(models.Model):
    cod_ibge = models.CharField(max_length=15)
    estado = models.CharField(max_length=30)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.estado


class Municipio(models.Model):
    cod_ibge = models.CharField(max_length=15)
    municipio = models.CharField(max_length=30)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['estado', 'municipio']
        ordering = ['municipio']

    def __str__(self):
        return self.municipio


class Grupo_Empresas(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Grupo_Empresas'

    def __str__(self):
        return self.descricao


class Unidade(models.Model):
    sigla = models.CharField(max_length=3)
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Desvio(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=14)
    un = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.valor) + ' ' + self.un.descricao
