# Generated by Django 3.2.3 on 2021-06-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank_master',
            name='dieselafter',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tank_master',
            name='lostdiesel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tank_master',
            name='lostdieselprice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tank_master',
            name='lostpetrol',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tank_master',
            name='lostpetrolprice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tank_master',
            name='petrolafter',
            field=models.FloatField(blank=True, null=True),
        ),
    ]