# Generated by Django 5.0.4 on 2024-04-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corefunctions', '0004_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('Shirt', 'Shirt'), ('T-Shirt', 'T-Shirt'), ('Pants', 'Pants')], max_length=255, null=True),
        ),
    ]
