# Generated by Django 5.0.6 on 2024-06-12 12:17

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=datetime.time(0, 0))),
                ('end_time', models.TimeField(default=datetime.time(0, 0))),
                ('image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/daluxpssk/image/upload/v1717835739/placeholderimage_ujh6em.svg', max_length=255, verbose_name='image')),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('name', 'description', 'location', 'start_date', 'end_date')},
            },
        ),
    ]
