# Generated by Django 2.2 on 2019-10-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_empresa_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
