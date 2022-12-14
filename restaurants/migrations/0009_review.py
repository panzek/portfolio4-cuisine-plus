# Generated by Django 4.1.2 on 2022-10-19 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_alter_restaurant_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(max_length=350, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approve', models.BooleanField(default=False)),
                ('restaurants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurants.restaurant')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
