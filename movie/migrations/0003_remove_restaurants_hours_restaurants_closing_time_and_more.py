# Generated by Django 4.2.4 on 2023-08-09 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurants',
            name='hours',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='closing_time',
            field=models.TimeField(default='18:00:00'),
        ),
        migrations.AddField(
            model_name='restaurants',
            name='opening_time',
            field=models.TimeField(default='07:00:00'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_description', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.restaurants')),
            ],
        ),
    ]