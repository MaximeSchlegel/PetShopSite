# Generated by Django 2.1.5 on 2019-01-18 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petshopmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='user_limit',
        ),
    ]
