# Generated by Django 5.0.4 on 2024-05-27 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_merge_20240526_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(max_length=100),
        ),
    ]
