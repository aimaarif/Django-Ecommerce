# Generated by Django 5.0.6 on 2024-06-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_alter_order_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
