# Generated by Django 5.0.4 on 2024-06-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corefunctions', '0020_alter_order_shipping_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discounted_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='title',
        ),
    ]
