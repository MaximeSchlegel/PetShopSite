# Generated by Django 2.1.5 on 2019-01-19 13:04

from django.db import migrations, models
import django.db.models.deletion
import petshopmanager.models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopmanager', '0006_auto_20190119_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='petshopmanager.Equipment', validators=[petshopmanager.models.validate_available]),
        ),
    ]
