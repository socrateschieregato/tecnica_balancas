# Generated by Django 2.2 on 2019-10-20 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20191016_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='tipo',
            new_name='tipo_tel',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='complemento',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='im',
        ),
    ]
