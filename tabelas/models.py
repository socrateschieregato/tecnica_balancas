from django.db import models


class Departamento(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Cargo(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


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
