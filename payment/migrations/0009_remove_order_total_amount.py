# Generated by Django 5.0.6 on 2024-06-01 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
    ]
