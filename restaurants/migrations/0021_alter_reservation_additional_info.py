# Generated by Django 4.1.2 on 2022-11-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0020_restaurant_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='additional_info',
            field=models.TextField(max_length=150, null=True),
        ),
    ]