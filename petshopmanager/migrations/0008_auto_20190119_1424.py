# Generated by Django 2.1.5 on 2019-01-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshopmanager', '0007_auto_20190119_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='last_move_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
