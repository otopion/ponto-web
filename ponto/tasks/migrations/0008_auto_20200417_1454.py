# Generated by Django 2.2.11 on 2020-04-17 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_funcionario_id_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='id_Usuario',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='sobre_nome',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
