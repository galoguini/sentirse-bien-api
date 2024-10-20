# Generated by Django 5.1 on 2024-10-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroPago', models.CharField(editable=False, max_length=15, unique=True)),
                ('fecha_pago', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
