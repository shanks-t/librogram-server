# Generated by Django 4.0 on 2022-01-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librogramapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='background_image_url',
            field=models.URLField(default=''),
        ),
    ]