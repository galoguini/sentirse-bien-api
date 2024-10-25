# Generated by Django 5.1 on 2024-10-25 00:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='usuario',
        ),
        migrations.AddField(
            model_name='turno',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnos_como_cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turno',
            name='profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turnos_como_profesional', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turno',
            name='hora',
            field=models.CharField(max_length=5),
        ),
    ]
