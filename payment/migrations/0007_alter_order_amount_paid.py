# Generated by Django 5.0.6 on 2024-05-31 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
