# Generated by Django 4.2.4 on 2024-01-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfc_app', '0031_requerimentoch_local_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requerimentoch',
            name='local_data',
            field=models.TextField(default='', max_length=50),
        ),
    ]
