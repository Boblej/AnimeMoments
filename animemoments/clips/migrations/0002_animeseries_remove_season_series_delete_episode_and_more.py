# Generated by Django 4.2.1 on 2024-08-01 19:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_title', models.CharField(max_length=255)),
                ('season_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('episode_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('episode_title', models.CharField(max_length=255)),
                ('episode_url', models.URLField()),
            ],
            options={
                'ordering': ['series_title', 'season_number', 'episode_number'],
                'unique_together': {('series_title', 'season_number', 'episode_number')},
            },
        ),
        migrations.RemoveField(
            model_name='season',
            name='series',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='Series',
        ),
    ]
