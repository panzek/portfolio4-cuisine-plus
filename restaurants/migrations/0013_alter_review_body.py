# Generated by Django 4.1.2 on 2022-10-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_alter_review_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
