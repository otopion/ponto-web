# Generated by Django 2.2.11 on 2020-06-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20200511_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='entrada_almoco',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='turno',
            name='saida_almoco',
            field=models.TimeField(null=True),
        ),
    ]
