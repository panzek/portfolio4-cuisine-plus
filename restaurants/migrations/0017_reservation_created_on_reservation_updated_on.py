# Generated by Django 4.1.2 on 2022-11-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0016_alter_reservation_number_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]