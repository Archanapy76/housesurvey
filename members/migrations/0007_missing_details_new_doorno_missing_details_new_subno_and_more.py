# Generated by Django 5.0.4 on 2024-05-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_missing_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing_details',
            name='new_doorno',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='missing_details',
            name='new_subno',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='missing_details',
            name='new_wardno',
            field=models.IntegerField(null=True),
        ),
    ]
