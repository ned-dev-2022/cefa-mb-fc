# Generated by Django 4.0 on 2022-05-14 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0007_actualite_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
