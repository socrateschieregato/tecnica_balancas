# Generated by Django 2.2 on 2019-09-25 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tabelas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_cnpj', models.CharField(max_length=14, verbose_name='CPF/CNPJ')),
                ('ie', models.CharField(max_length=12, verbose_name='Inscrição Estadual')),
                ('nome_razao', models.CharField(max_length=100, verbose_name='Nome/Razão')),
                ('nome_fantasia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome Fantasia')),
                ('email', models.CharField(max_length=50)),
                ('im', models.CharField(blank=True, max_length=8, null=True)),
                ('dt_criacao', models.DateTimeField(auto_now=True)),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tabelas.Grupo_Empresas')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Fone'), ('2', 'Cel'), ('3', 'Outro')], default='1', max_length=10)),
                ('ddd', models.CharField(blank=True, max_length=2, null=True, verbose_name='DDD')),
                ('num_tel', models.CharField(blank=True, max_length=10, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_log', models.CharField(choices=[('1', 'Rua'), ('2', 'Av'), ('3', 'Rod'), ('4', 'Outro')], default='1', max_length=10)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(blank=True, max_length=30, null=True)),
                ('complemento', models.CharField(blank=True, max_length=30, null=True)),
                ('cep', models.CharField(max_length=9)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tabelas.Municipio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tabelas.Pais')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tabelas.Estado')),
            ],
        ),
    ]
