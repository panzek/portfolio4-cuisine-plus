# Generated by Django 4.1.2 on 2022-10-31 09:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
