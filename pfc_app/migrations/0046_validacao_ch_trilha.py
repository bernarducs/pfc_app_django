# Generated by Django 4.2.4 on 2024-01-18 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfc_app', '0045_carreira_validacao_ch_carreira'),
    ]

    operations = [
        migrations.AddField(
            model_name='validacao_ch',
            name='trilha',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pfc_app.trilha'),
        ),
    ]
