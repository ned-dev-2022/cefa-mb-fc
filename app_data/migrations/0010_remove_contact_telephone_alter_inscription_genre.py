# Generated by Django 4.0 on 2022-05-14 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0009_alter_inscription_choix_cefa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='inscription',
            name='genre',
            field=models.CharField(max_length=20),
        ),
    ]
