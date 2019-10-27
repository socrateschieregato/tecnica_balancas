from django.db import models

tipos_tel = (('Fone', 'Fone'), ('Cel', 'Cel'), ('Outro', 'Outro'))
tipos_log = (('Rua', 'Rua'), ('Av', 'Av'), ('Rod', 'Rod'), ('Outro', 'Outro'))


class Empresa(models.Model):
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14, unique=True)
    ie = models.CharField('Inscrição Estadual', max_length=14, null=True, blank=True)
    nome_razao = models.CharField('Nome/Razão', max_length=100)
    nome_fantasia = models.CharField(
        'Nome Fantasia',
        max_length=50,
        null=True,
        blank=True
    )
    email = models.CharField(max_length=50, null=True, blank=True)
    dt_criacao = models.DateTimeField(auto_now=True)
    tipo_log = models.CharField(max_length=10, choices=tipos_log, default='1', null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=30, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=30, null=True, blank=True)
    municipio = models.CharField(max_length=50, null=True, blank=True)
    tipo_tel = models.CharField(max_length=10, choices=tipos_tel, default='1', null=True, blank=True)
    ddd = models.CharField('DDD', max_length=2, null=True, blank=True)
    num_tel = models.CharField(max_length=10, null=True, blank=True)
    unidade = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome_fantasia
