# Generated by Django 5.1 on 2024-10-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='monto',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
