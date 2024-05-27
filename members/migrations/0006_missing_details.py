# Generated by Django 5.0.4 on 2024-05-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_avilabe_data_delete_assesment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missing_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('owner_PhoneNumber', models.CharField(max_length=20)),
                ('occupier_address', models.CharField(max_length=200)),
                ('ground_floor', models.CharField(max_length=50)),
                ('first_floor', models.CharField(max_length=50)),
                ('total', models.CharField(max_length=50)),
                ('difference', models.CharField(max_length=50)),
                ('percent_difference', models.CharField(max_length=50)),
                ('building_usage', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=255)),
            ],
        ),
    ]