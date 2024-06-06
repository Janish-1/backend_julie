# Generated by Django 5.0.4 on 2024-05-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corefunctions', '0012_alter_product_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='pants_measurement_length',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='pants_measurement_waist',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='pant_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='pant_measurement_waist',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='style',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='chudidar_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='chudidar_measurement_waist',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='coat_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='coat_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='jacket_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='jacket_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='kameej_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='kameej_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='kurta_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='kurta_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='nehrujacket_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='nehrujacket_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pajama_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pajama_measurement_waist',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pathani_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='pathani_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='shirt_measurement_chest',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='shirt_measurement_length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]