# Generated by Django 4.2.4 on 2023-08-09 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_remove_restaurants_hours_restaurants_closing_time_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Restaurants',
        ),
    ]