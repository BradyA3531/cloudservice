# Generated by Django 5.0.3 on 2024-03-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_', '0002_data_file_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
