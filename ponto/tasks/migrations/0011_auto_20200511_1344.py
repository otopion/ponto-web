# Generated by Django 2.2.11 on 2020-05-11 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_funcionario_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='entrada_almoço',
            new_name='entrada_almoco',
        ),
        migrations.RenameField(
            model_name='turno',
            old_name='saida_almoço',
            new_name='saida_almoco',
        ),
    ]
