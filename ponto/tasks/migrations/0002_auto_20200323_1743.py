# Generated by Django 2.2.11 on 2020-03-23 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='presente',
            new_name='presentee',
        ),
    ]
