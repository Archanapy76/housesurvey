# Generated by Django 5.0.4 on 2024-05-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_delete_missing_details_avilabe_data_building_usage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avilabe_data',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='avilabe_data',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
