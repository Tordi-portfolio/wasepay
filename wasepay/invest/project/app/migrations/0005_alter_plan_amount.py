# Generated by Django 5.2.3 on 2025-06-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='amount',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=12),
        ),
    ]
