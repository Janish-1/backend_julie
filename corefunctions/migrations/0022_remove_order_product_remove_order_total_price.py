# Generated by Django 5.0.4 on 2024-06-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corefunctions', '0021_remove_order_discounted_price_remove_order_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]