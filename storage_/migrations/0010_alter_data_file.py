# Generated by Django 5.0.3 on 2024-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_', '0009_alter_data_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d'),
        ),
    ]
