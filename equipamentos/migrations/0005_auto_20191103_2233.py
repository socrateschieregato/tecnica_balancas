# Generated by Django 2.2 on 2019-11-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0004_auto_20191022_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
