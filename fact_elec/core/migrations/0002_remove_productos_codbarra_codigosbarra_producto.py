# Generated by Django 4.2.16 on 2024-10-31 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='codbarra',
        ),
        migrations.AddField(
            model_name='codigosbarra',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.productos'),
        ),
    ]
