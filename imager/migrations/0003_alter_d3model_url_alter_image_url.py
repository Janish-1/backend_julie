# Generated by Django 5.0.4 on 2024-04-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager', '0002_d3model_alter_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d3model',
            name='url',
            field=models.FileField(upload_to='media/3dmodels/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='media/'),
        ),
    ]