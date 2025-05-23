# Generated by Django 5.0.4 on 2024-04-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assesment',
            name='ground_area',
        ),
        migrations.AddField(
            model_name='assesment',
            name='ground_floorarea',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assesment',
            name='door_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='first_floorarea',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='floor_area',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='new_subno',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='total',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='assesment',
            name='ward_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='field',
            name='Total',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='field',
            name='first_floorarea',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='field',
            name='floor_area',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='field',
            name='ground_floorarea',
            field=models.CharField(max_length=200),
        ),
    ]
