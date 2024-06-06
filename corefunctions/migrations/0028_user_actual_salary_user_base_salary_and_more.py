# Generated by Django 5.0.4 on 2024-06-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corefunctions', '0027_leave_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='actual_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='base_salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='leaves_taken',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]